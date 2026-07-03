from fastapi import FastAPI

app = FastAPI(title="GnomoVerde")


@app.get("/")
def root():
    return {
        "project": "GnomoVerde",
        "status": "online"
    }