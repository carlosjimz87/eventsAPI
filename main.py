import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from api.router import router

app = FastAPI(
    title="Events API Fever",
    description="This is a Python based API to retrieve events information from an external provider.",
    version="1.0.0",
)


app.include_router(router)

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)
