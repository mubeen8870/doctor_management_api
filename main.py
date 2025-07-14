from fastapi import FastAPI
from routes import router as doctor_router

app = FastAPI(title="Doctor Management API")

app.include_router(doctor_router)
