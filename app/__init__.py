from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(title="Ayurvedic Consultation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000" ,
                   'https://frontend-dot-ayurguide-451219.uc.r.appspot.com' ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Remove the prefix here - don't include it in app.include_router
app.include_router(router)  # Remove prefix="/api/v1"
