from fastapi import FastAPI, Request, Depends, status, Form, Response, Path
from sqlalchemy.orm import Session
from app.model import *
from app.schema import *
from app.db import *
from app.config import *
import redis

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_cache():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0)
    try:
        yield r
    finally:
        r.close()

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
def create_prediction(id:int, variable: dict, db: Session = Depends(get_db), r = Depends(get_cache)):
    

    # If the prediction is already in the cache, return the prediction
    if r.get(id):
        static_prediction = r.get(id)
        predication = Predictions(id=int(id), variables=variable, prediction=static_prediction)
        return predication
    else:

        # Generate model predications
        static_prediction = "static prediction"
        
        # Store the data in the database
        prediction = Predictions(id=int(id), variables=variable, prediction=static_prediction)
        db.add(prediction)
        db.commit()
        db.refresh(prediction)

        # Update the cache
        r.set(id, str(prediction.prediction))


        return prediction