from fastapi import FastAPI
from routes.opus_en_fr_router import opus_en_fr_router

app = FastAPI()

app.include_router(opus_en_fr_router)