import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

## url vers l'api
URL_API= "https://api-risk.onrender.com/"
st.set_page_config(page_title='ScoringApp', page_icon="images.jpeg", layout='wide', initial_sidebar_state="expanded")

st.sidebar.title('Menu')
menu = st.sidebar.radio("Go to :", ["Home", "Predictions", "Visualisations"])


if menu =="Home":
    message_welcome = f"""
    You're welcome at ScoringApp !"""
    st.title(message_welcome)
    st.image("risque.png", caption="Risque de creddit",channels="RGB", use_container_width=True)    
elif menu =="Predictions":
    
    st.title(" Niveau de risque ? Probabilité ? Vous etes ouverts à tous !")
    st.image("predit.png", caption="Evaluation risque",channels="RGB", use_container_width=True, output_format="auto")    

    
    st.write(f"""  #### Etes vous dans une situation dont vous ne savez pas si votre non remboursement de crédit bancaire sera pénal ou non ?
             
            ### Eh bien ! C'est le moment de le savoir pour prendre les dispositions nécéssaires. """)
            
    
    st.sidebar.header("Entrer de nouvelles données")
    data_scoring = {
    "Age": st.sidebar.number_input("Âge", min_value=18, max_value=100, value=30),
    "Sex": st.sidebar.selectbox("Sexe", ["Male", "Female"]),
    "Job": st.sidebar.number_input("Job", min_value=0, max_value=3, value=0),
    "Housing": st.sidebar.selectbox("Logement", ["own", "free", "rent"]),
    "Saving accounts": st.sidebar.selectbox("Comptes épargne", ["little", "moderate", "rich", "NA"]),
    "Checking account": st.sidebar.selectbox("Comptes courant", ["little", "moderate", "rich", "NA"]),
    "Credit amount": st.sidebar.number_input("Montant crédit", min_value=0.0, value=2000.0),
    "Duration": st.sidebar.number_input("Durée", min_value=1, max_value=72, value=12),
    "Purpose": st.sidebar.selectbox("But", ["education", "car", "business", "domestic appliances", "repairs", "radio/TV", "vacation/others"]),
}
    try:
        if st.sidebar.button("Faire une prédiction"):
            response = requests.post(f"{URL_API}/predict", json=data_scoring)
            if response.status_code == 200:
                prediction = pd.DataFrame(response.json())
            st.write("### Résultat de la Prédiction", prediction)
            #st.json('Le risque de score est : ', prediction.to_json()
    except Exception as e:
        st.error(f'Veuillez verifier les données entrées {str(e)}')

elif menu=='Visualisations':

    st.title("Tableau de bord des Résultats de Modélisation")
    try :
        # Section pour uploader le fichier CSV combiné
        uploaded_file = st.file_uploader("Chargez votre le fichier de prédiction au format CSV :", type=["csv"])

        if uploaded_file:
            # Envoi des données vers l'API
            with st.spinner("Chargement du fichier ..."):
                response = requests.post(f"{URL_API}/stats", files={"file": uploaded_file})
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data["status"] == "success":
                        data= pd.DataFrame(response_data["data"])
                        st.success("Données chargées avec succès !")
                        
                        ### pour la classe normale
                        
                        fig = px.histogram(data, x="Normal", color="Predicted", 
                                        title="Distribution du risque normale par Classe")
                        st.plotly_chart(fig)
                        
                        
                        fig = px.pie(data, names="Normal", color="Predicted",
                                     title="Répartition des Classes Normales")
                        st.plotly_chart(fig)
                        
                        # pour les probabilites et les classes predictes
                        fig = px.histogram(data, x="Probability", color="Predicted", 
                                        title="Distribution des Probabilités par Classe")
                        st.plotly_chart(fig)

                        # Pie chart pour les prédictions
                        #st.write("## Répartition des Prédictions :")
                        fig = px.pie(data, names="Predicted", title="Répartition des Classes Prédictes")
                        st.plotly_chart(fig)
                        
                      # Création du graphique avec Plotly
                        fig = px.box(data, x='Normal', y='Probability', color='Predicted', color_discrete_sequence=px.colors.qualitative.Set3,
                                     title="Répartition entre le risque normal et la probabilité ")

                        # Afficher dans Streamlit
                        st.plotly_chart(fig)
                        
                        figure = px.scatter(data, x='Normal', y='Predicted',
                                            title='Nuages de point entre les données normales et prédites',
                                            color='Predicted', color_discrete_sequence=px.colors.qualitative.Set3)
                        st.plotly_chart(figure)

                    else:
                        st.error(f"Erreur : {response_data['message']}")
    except Exception as e:
        st.error(f"Échec de la connexion à l'API. Code HTTP")
