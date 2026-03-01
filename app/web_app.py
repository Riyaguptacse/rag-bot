
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .rag_chatbot import rag_answer, chat_memory
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use absolute path for static
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "../static")), name="static")


templates = Jinja2Templates(directory="templates")

# Serve static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "chat": chat_memory})

@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, question: str = Form(...)):
    answer = rag_answer(question)
    return templates.TemplateResponse("chat.html", {"request": request, "chat": chat_memory})