from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.auth import router as auth_router
from api.routes.history import router as history_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(history_router, prefix="/history", tags=["history"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}