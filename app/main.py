from fastapi import FastAPI
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from app.api.v1.router import router
from app.core.config import CORS
from fastapi.middleware.cors import CORSMiddleware
from app.core.limiter import limiter

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS,           
    allow_credentials=True,       
    allow_methods=["*"],            
    allow_headers=["*"],         
)

app.include_router(router, prefix="/api/v1")
