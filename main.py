from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from routes.route import route
from sqlalchemy.orm import session
from config.db import engine
from models import model
# import uvicorn

model.Base.metadata.create_all(engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(route) 

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)