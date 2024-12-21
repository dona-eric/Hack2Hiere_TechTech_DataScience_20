from fastapi import FastAPI, HTTPException,UploadFile, File
from pydantic import BaseModel, Field
import pandas as pd
import requests
import joblib, pickle, io
from fastapi.responses import JSONResponse

app = FastAPI()

### load the models
transformer = joblib.load('../models_credit_risque/pipeline_transformer.pkl')
model = joblib.load('../models_credit_risque/final_model_pipeline.pkl')
# create a class of database who will be used to print the results of prediction about streamlit interfaceing

class DataScoring(BaseModel):
    Age:int
    Sex: str
    Job:int
    Housing: str
    Saving_accounts: str | None = Field(None, alias="Saving accounts")
    Checking_account: str | None = Field(None, alias="Checking account")
    Credit_amount: int = Field(..., alias="Credit amount")
    Duration:int
    Purpose:str
    
    
    class Config:
        alias_generator = lambda field: field.replace("_", " ")
        allow_population_by_name = True
        
@app.post('/predict')
def predict(data: DataScoring):
    
    df_dict = data.dict(by_alias=True)
    df = pd.DataFrame([df_dict])
    ## apply the model to get the predictions and probabilities
    
    try:
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]
        labels = ["Good" if pred ==1 else "Bad" for pred in predictions]
        #save the results
        result = df.copy()
        result['prediction'] = labels
        result['probability']= probabilities
        return result.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Veuillez saisir des données valides ! {str(e)}")


#routes pour les visualisations

@app.post("/stats")
async def load_file(file: UploadFile = File(...)):
    try:
        # Lire le fichier CSV
        content = await file.read()
        data = pd.read_csv(io.BytesIO(content))
        
        # Convertir en JSON
        data_json = data.to_dict(orient="records")
        return {"status": "success", "data": data_json}
    except Exception as e:
        return {"status": "error", "message": str(e)}
