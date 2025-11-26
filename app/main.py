import logging
import time
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .schemas import ChatRequest, ChatResponse
from .agent import agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("chat-agent")

app = FastAPI(
    title="Chat Agent API",
    version="1.0.0",
    description="API de Chat conectada a um Agente de IA usando Strands + Ollama",
)

# Caminho da pasta static
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

# Monta /static para servir CSS/JS/HTML, se quiser
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index():
    """
    Retorna a página simples de chat.
    """
    index_file = STATIC_DIR / "index.html"
    return FileResponse(index_file)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    logger.info(f"[REQUEST] Mensagem recebida: {payload.message!r}")

    if any(op in payload.message for op in ["+", "-", "*", "/", "%"]) and any(
        ch.isdigit() for ch in payload.message
    ):
        logger.info(
            "[HINT] Mensagem parece conter operação matemática. "
            "É provável que o agente use a tool 'calculator'."
        )

    start = time.time()
    result = agent(payload.message)
    duration = time.time() - start

    logger.info(f"[RESPONSE] Resposta gerada em {duration:.2f}s: {result!r}")
    logger.info(f"[METRICS] Tempo de resposta: {duration:.2f}s")

    return ChatResponse(response=str(result))
