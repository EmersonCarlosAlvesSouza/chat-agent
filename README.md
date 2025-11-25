# chat-agent

Projeto de API de chat usando **FastAPI** + **Strands Agents** + **Ollama**, desenvolvido como solução para o desafio técnico.

O agente de IA é capaz de:
- Responder perguntas de **conhecimento geral** (sem usar ferramentas externas).
- Identificar quando a pergunta exige **cálculo matemático** e, nesses casos, utilizar a tool `calculator` do Strands para obter o resultado com precisão.

---

## 📁 Estrutura do projeto

```bash
chat-agent/
├── app/
│   ├── __init__.py
│   ├── agent.py          # Configuração do agente Strands + Ollama + tools
│   ├── config.py         # Leitura das variáveis de ambiente (.env)
│   ├── main.py           # Aplicação FastAPI (endpoints)
│   └── schemas.py        # Modelos Pydantic de request/response
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore
├── README.md
└── requirements.txt

✅ Pré-requisitos

Python 3.10+ instalado

Ollama instalado localmente
👉 Documentação: https://ollama.com

⚙️ Configuração do ambiente
1. Clonar o repositório

git clone https://github.com/EmersonCarlosAlvesSouza/chat-agent.git
cd chat-agent
2. Criar e ativar o ambiente virtual
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Linux / macOS
source .venv/bin/activate

3. Instalar dependências
pip install -r requirements.txt

4. Instalar o modelo no Ollama

Exemplo usando o modelo llama3.1:

ollama pull llama3.1

5. Configurar variáveis de ambiente

Copie o arquivo de exemplo:

cp .env.example .env


Edite o arquivo .env se quiser alterar alguma configuração:

# Ollama configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL_ID=llama3.1:latest

# Agent configuration
AGENT_SYSTEM_PROMPT=Você é um assistente útil que responde em português do Brasil. Para perguntas gerais (história, biografias, ciência, curiosidades, etc.), responda normalmente SEM usar ferramentas. Use a ferramenta de cálculo `calculator` SOMENTE quando a pergunta envolver cálculos matemáticos numéricos explícitos (operações, raízes, potências, porcentagens, etc.). Ao chamar a ferramenta, passe apenas a expressão matemática bruta, por exemplo: "1234 * 5678" ou "sqrt(144)", sem texto extra. Nunca chame a ferramenta `calculator` para perguntas sobre pessoas, história ou conceitos não numéricos.

🚀 Executando a API

Com o ambiente virtual ativado e o Ollama rodando:

uvicorn app.main:app --reload


A API ficará disponível em:

http://localhost:8000

Documentação automática do FastAPI (opcional):

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

📡 Endpoint de Chat
POST /chat

Request body (application/json):

{
  "message": "Quanto é 1234 * 5678?"
}


Response body:

{
  "response": "7021792"
}

Exemplo usando curl

Pergunta de cálculo (usa a tool calculator):

curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Quanto é 1234 * 5678?\"}"


Pergunta de conhecimento geral (NÃO usa tool):

curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Quem foi Albert Einstein?\"}"

🧠 Lógica do Agente

O agente é configurado em app/agent.py:

Modelo: OllamaModel, configurado via variáveis de ambiente.

Tool registrada: calculator (strands-agents-tools).

O comportamento é controlado pelo AGENT_SYSTEM_PROMPT, que instrui:

Quando usar a tool de cálculo (expressões matemáticas explícitas).

Quando não usar a tool (perguntas gerais, biografias, conceitos, etc.).

📝 Observações

O projeto foi estruturado para ser simples de executar e fácil de ler, destacando:

Separação entre configuração (config.py), agente (agent.py), API (main.py) e schemas (schemas.py).

Uso de .env e .env.example para configuração do ambiente.

Boas práticas básicas de FastAPI e Pydantic.
