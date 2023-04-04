from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
async def greeting(name: str = "World"):
    return {"message": f"Hello, {name}!"}