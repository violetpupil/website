from fastapi import FastAPI

app = FastAPI()


@app.get("/popular")
def popular():
    return "index"
