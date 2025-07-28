from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def test():
    return {"message":"hello world"}


@app.get("/integer_info")
def send_integer():
    
    return {"message":1}