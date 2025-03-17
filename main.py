from fastapi import FastAPI
from app.generators import text_generator, image_generator

app = FastAPI(title="AI Social Media Agent API")

app.include_router(text_generator.router, prefix="/api")
app.include_router(image_generator.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AI Social Media Agent API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
