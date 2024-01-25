from fastapi import APIRouter, Form, Request, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from config.db import get_db
from models import model

route = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_task(db):
    tasks = db.query(model.Task).all()
    return tasks

def add_task(name, description, db):
    new_task = model.Task(name=name, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {True}

def delete_task(name, db):
    db.query(model.Task).filter(model.Task.name == name).delete(synchronize_session=False)
    db.commit()
    return {True}



@route.get("/", response_class=HTMLResponse)
async def homepage(request: Request, db: Session = Depends(get_db)):
    tasks= get_task(db)
    return templates.TemplateResponse("index.html", {"request":request, "tasks": tasks})

@route.post("/", response_class=HTMLResponse)
def post_task(name: str=Form(), description: str=Form(), db: Session = Depends(get_db)):
    add_task(name, description, db)
    return RedirectResponse("/",status_code=status.HTTP_303_SEE_OTHER)

@route.get("/delete/{name}", response_class=HTMLResponse)
def remove_task(name:str, db: Session = Depends(get_db)):
    delete_task(name, db)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
