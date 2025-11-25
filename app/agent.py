from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator


from .config import OLLAMA_HOST, OLLAMA_MODEL_ID, AGENT_SYSTEM_PROMPT

# Configura o modelo local do Ollama
ollama_model = OllamaModel(
    host=OLLAMA_HOST,
    model_id=OLLAMA_MODEL_ID,
)

# Cria o agente de IA
agent = Agent(
    model=ollama_model,
    tools=[calculator],          # Tool de cálculo matemático
    system_prompt=AGENT_SYSTEM_PROMPT,
)
