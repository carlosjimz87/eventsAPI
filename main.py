import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.router import router
from models.errors import MissingDateParameter
from utils.remove_errors import remove_422s

app = FastAPI(
    title="Events API Fever",
    description="This is a Python based API to retrieve events information from an external provider.",
    version="1.0.0",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "error": {
                    "code": "400",
                    "message": "query parameter has wrong format",
                },
                "data": None,
            }
        ),
    )


@app.exception_handler(MissingDateParameter)
async def missing_date_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "error": {
                    "code": "400",
                    "message": "Missing query parameter",
                },
                "data": None,
            }
        ),
    )


app.include_router(router)
remove_422s(app)

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)
