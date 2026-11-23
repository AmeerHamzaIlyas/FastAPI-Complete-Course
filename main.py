from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{"message": "Hi Ameer"}
    

@app.get("/about")
def about():
    return{"message": "Hi this is demo api that define what we can write in out about section"}

@app.get("/about/id")
def id():
    return{"message": "this is id"}
