from fastapi import FastAPI, Request, Depends, status, Form, Response, Path
from sqlalchemy.orm import Session
from app.model import *
from app.schema import *
from app.db import *

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return "Welcome to Clustering Inference API :)"


# return model results
@app.get("/predictions", response_model=List[PredictionBase])
def predict():
     # get data from database
    with DBContext() as db:
        results = db.query(Predictions).all()
        return results


@app.post("/predictions", response_model=PredictionBase, status_code=status.HTTP_201_CREATED)
def create_prediction(variable: dict, db: Session = Depends(get_db)):
    static_prediction = "static prediction"
    prediction = Predictions(variables=variable, prediction=static_prediction)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction