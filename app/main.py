from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Clustering Inference API :)"


# return model results
@app.get("/predict")
def predict():
    return "This is a predictionpoetry