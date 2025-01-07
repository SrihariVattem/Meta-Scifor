from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return templates.TemplateResponse("home.html", {"request": request, "blogs": blogs})

@app.get("/add-blog")
async def add_blog_form(request: Request):
    return templates.TemplateResponse("add_blog.html", {"request": request})

@app.post("/add-blog")
async def add_blog(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    new_blog = models.Blog(title=title, content=content)
    db.add(new_blog)
    db.commit()
    return RedirectResponse("/", status_code=303)
