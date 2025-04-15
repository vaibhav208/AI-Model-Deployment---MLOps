from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

class Input(BaseModel):
    data: list

@app.post("/predict")
def predict(input: Input):
    prediction = model.predict(np.array(input.data).reshape(1, -1))
    return {"prediction": int(prediction[0])}