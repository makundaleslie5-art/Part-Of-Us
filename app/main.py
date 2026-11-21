from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Part Of Us",
    description="Together We Grow",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"active_page": "home"}
    )


@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"active_page": "about"}
    )


@app.get("/programmes")
async def programmes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="programmes.html",
        context={"active_page": "programmes"}
    )


@app.get("/impact")
async def impact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="impact.html",
        context={"active_page": "impact"}
    )


@app.get("/get-involved")
async def get_involved(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="get_involved.html",
        context={"active_page": "involved"}
    )


@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"active_page": "contact"}
    )


@app.get("/health")
async def health():
    return {"status": "Part Of Us is running"}
