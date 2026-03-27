from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# To run this application, use the command: uvicorn app.main:app --reload