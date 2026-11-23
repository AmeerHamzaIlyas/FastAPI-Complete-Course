from fastapi import FastAPI
import json
app = FastAPI()

# load our data 
def load_data():
    with open("Patients.json", "r") as f:
        data = json.load(f)
    return data



@app.get('/')
def home():
    return{"message": "Hi Ameer"}
    

@app.get("/about")
def about():
    return{"message": "Hi this is demo api that define what we can write in out about section"}

@app.get("/view")
def view():
    data = load_data()
    return data


