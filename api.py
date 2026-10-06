import uvicorn

from src.endpoints.create_user import router as new_user_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(new_user_router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1",
                port=8000,
                reload=True)