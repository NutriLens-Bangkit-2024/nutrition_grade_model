from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_nutriscore

app = FastAPI()

class NutritionIn(BaseModel):
    energi : float
    protein : float
    lemak : float
    karbohidrat : float
    serat : float
    natrium : float

class PredictionOut(BaseModel):
    score : str

@app.get("/")
def home():
    return {"health_check" : "OK"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: NutritionIn):
    score = predict_nutriscore(payload.energi, 
                               payload.protein, 
                               payload.lemak,
                               payload.karbohidrat,
                               payload.serat,
                               payload.natrium)
    return {"score" : score}