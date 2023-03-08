from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return 'Hello!'

@app.get('/add')
def add(n: int = None , j: int = None):
    if n>=0 & j>=0:
        sum=0
        sum=n+j
        return {
            "Sum":sum,
            "Number1":n,
            "Number2":j,
        }
    else:
        return {"Error": "NO NEGATIVE ADDITIONS FOR NOW!!"}