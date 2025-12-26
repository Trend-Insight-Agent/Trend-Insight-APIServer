from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Trend Insight API Server"}

@app.get("/health")
def read_health():
    return {"status": "ok"}
