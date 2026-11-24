from fastapi import FastAPI, Path
import json


app = FastAPI()

# load our data 
def load_data():
    with open("Patients.json", "r") as f:
        data = json.load(f)
    return data



@app.get('/')
def home():
    return{"message": "Patient Managment System (PMS) API"}
    

@app.get("/about")
def about():
    return{"message": "This is all about PMS system"}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def patient_view(patient_id: str = Path (..., description="ID of the Patient",example="p1")):
    # Load our data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"Patient not found"}

