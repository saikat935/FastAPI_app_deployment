from fastapi import FastAPI

app = FastAPI(title="Azure VM FastAPI Application")

@app.get("/")
def home():
    return {
        "message": "FastAPI is running on Azure VM!",
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}