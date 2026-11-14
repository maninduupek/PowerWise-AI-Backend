
from fastapi import FastAPI

from app.routes import dashboard, analytics

app = FastAPI(
    title="PowerWise AI API",
    description="Backend API for household energy monitoring",
    version="1.0.0"
)

# Register API routes
app.include_router(dashboard.router)
app.include_router(analytics.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to PowerWise AI Backend!",
        "status": "Running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "PowerWise AI"
    }
