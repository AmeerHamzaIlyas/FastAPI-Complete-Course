from fastapi import FastAPI, Path, HTTPException,Query
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
        # {"error","patient not found"}
        raise HTTPException(status_code=404, detail="Patient not found")
# sort API
    
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of name or admitted_date"),
                  order: str = Query("asc", description="arrangeby asc or des order")):
    sort_fields = ["name","admitted_date"]
    if sort_by not in sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {sort_fields}")
    if order not in ["asc", "des"]:
        raise HTTPException(status_code=400, detail="Invalid field select from asc or des")
    
    data = load_data()
    
    sort_order = True if order == "des" else False
    
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0), reverse = sort_order)
    
    return sorted_data