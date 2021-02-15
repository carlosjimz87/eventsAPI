from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get():
    return "{'hello':'hello fastapi'}"
