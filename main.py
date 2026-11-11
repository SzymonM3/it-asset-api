from fastapi import FastAPI

app = FastAPI(
    title="IT Asset Inventory API",
    description="A REST API for managing IT assets.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "IT Asset Inventory API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
