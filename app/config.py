import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL_ID = os.getenv("OLLAMA_MODEL_ID", "llama3")

AGENT_SYSTEM_PROMPT = os.getenv(
    "AGENT_SYSTEM_PROMPT",
    (
        "Você é um assistente útil que responde em português do Brasil. "
        "Você sabe responder perguntas gerais e, quando a pergunta envolver "
        "cálculos matemáticos, você usa a ferramenta de cálculo disponível "
        "para garantir a exatidão do resultado."
    ),
)
