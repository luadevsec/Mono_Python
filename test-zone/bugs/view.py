from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

def home(request) -> HTMLResponse:
    return templates.TemplateResponse('home.html',{"request": request})
