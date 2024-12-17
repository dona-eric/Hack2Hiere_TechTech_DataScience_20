import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

## url vers l'api
URL_API= "http://127.0.0.1:8000/"
st.set_page_config(page_title='ScoringApp', page_icon=":shark", layout='wide', initial_sidebar_state="expanded")

st.sidebar.title('Menu')
menu = st.sidebar.radio("Go to :", ["Home", "Predictions", "Visualisations"])

if menu =="Home":
    message_welcome = f"""
    You're welcome at ScoringApp !"""
    st.title(message_welcome)
    
elif menu =="Predictions":
    st.title('DASHBORD')
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
        #else:
        #    st.error("Erreur lors de la prédiction.")
        if st.sidebar.button("Visualisations"):
            response = requests.get(f'{URL_API}/stats', json=data_scoring)
            if response.status_code==200:
                visualiation = response.json()
                st.write('### Visualisations:', visualiation)
    except Exception as e:
        st.error(f'Veuillez verifier les données entrées {str(e)}')
    
    