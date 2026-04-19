from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="Бон Бон Праздник")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Примеры праздников (фото и видео с интернета)
gallery_items = [
    {"type": "image", "url": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=600", "title": "Детский день рождения"},
    {"type": "image", "url": "https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=600", "title": "Свадебное торжество"},
    {"type": "image", "url": "https://images.unsplash.com/photo-1472653431158-6364773b2a56?w=600", "title": "Выпускной вечер"},
    {"type": "image", "url": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=600", "title": "Корпоратив"},
    {"type": "image", "url": "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=600", "title": "Новогодний утренник"},
    {"type": "video", "url": "https://www.youtube.com/embed/1Z1E7nR3l8E", "title": "Как мы организуем праздники"},
    {"type": "video", "url": "https://www.youtube.com/embed/8Pmv_2K5gKA", "title": "Лучшие моменты 2024"},
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "active": "home"})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "active": "about"})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "active": "contact"})

@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    return templates.TemplateResponse("gallery.html", {
        "request": request,
        "active": "gallery",
        "gallery_items": gallery_items
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)