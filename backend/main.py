from fastapi import FastAPI

app = FastAPI(title="Kitchen Assistant")


@app.get("/health")
def health():
    return {"status": "ok"}
