# import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.main_router import router as api_router
#import os
#import logging

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

#uvicorn main:app --host 0.0.0.0 --port 8005