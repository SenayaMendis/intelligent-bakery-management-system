from fastapi import FastAPI

app = FastAPI(title="Bakery ML Service")

@app.get("/health")
def health_check():
    return {"message": "Bakery ML service is running"}