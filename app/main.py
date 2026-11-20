from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(
    title="Part Of Us",
    description="Together We Grow",
    version="1.0.0"
)

# Connect static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect HTML templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={}
    )


@app.get("/health")
async def health():
    return {"status": "Part Of Us is running"}
