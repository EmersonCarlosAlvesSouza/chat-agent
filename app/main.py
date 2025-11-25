from fastapi import FastAPI
from .schemas import ChatRequest, ChatResponse
from .agent import agent

app = FastAPI(
    title="Chat Agent API",
    version="1.0.0",
    description="API de Chat conectada a um Agente de IA usando Strands + Ollama",
)


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    """
    Endpoint principal do chat.
    Recebe: {"message": "..."}
    Retorna: {"response": "..."}
    """

    # Chamada simples ao agente do Strands
    result = agent(payload.message)

    return ChatResponse(response=str(result))
