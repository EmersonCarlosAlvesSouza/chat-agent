# chat-agent

Projeto de API de chat usando **FastAPI** + **Strands Agents** + **Ollama**, desenvolvido como solução para o desafio técnico.

O agente de IA é capaz de:
- Responder perguntas de **conhecimento geral** (sem usar ferramentas externas).
- Identificar quando a pergunta exige **cálculo matemático** e, nesses casos, utilizar a tool `calculator` do Strands para obter o resultado com precisão.
- Oferecer uma **interface web simples** para interação direta com a API, sem necessidade de Postman.

---

## 📁 Estrutura do projeto

```bash
chat-agent/
├── app/
│   ├── __init__.py
│   ├── agent.py          # Configuração do agente Strands + Ollama + tools
│   ├── config.py         # Leitura das variáveis de ambiente (.env)
│   ├── main.py           # Aplicação FastAPI (endpoints + página HTML + healthcheck)
│   └── schemas.py        # Modelos Pydantic de request/response
├── static/
│   └── index.html        # Interface web simples para conversar com o agente
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore
├── README.md
└── requirements.txt
```

✅ Pré-requisitos

Python 3.10+ instalado

Ollama instalado localmente
👉 Documentação: https://ollama.com

⚙️ Configuração do ambiente
1. Clonar o repositório

```bash
git clone https://github.com/EmersonCarlosAlvesSouza/chat-agent.git
cd chat-agent
```

2. Criar e ativar o ambiente virtual
```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Linux / macOS
source .venv/bin/activate
```

3. Instalar dependências
```bash
pip install -r requirements.txt
```
4. Instalar o modelo no Ollama

Exemplo usando o modelo llama3.1:
```bash
ollama pull llama3.1
```
5. Configurar variáveis de ambiente

Copie o arquivo de exemplo:
```bash
cp .env.example .env
```
Edite o arquivo .env se quiser alterar alguma configuração:
```bash
# Ollama configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL_ID=llama3.1:latest

# Agent configuration
AGENT_SYSTEM_PROMPT=Você é um assistente útil que responde em português do Brasil. Para perguntas gerais (história, biografias, ciência, curiosidades, etc.), responda normalmente SEM usar ferramentas. Use a ferramenta de cálculo `calculator` SOMENTE quando a pergunta envolver cálculos matemáticos numéricos explícitos (operações, raízes, potências, porcentagens, etc.). Ao chamar a ferramenta, passe apenas a expressão matemática bruta, por exemplo: "1234 * 5678" ou "sqrt(144)", sem texto extra. Nunca chame a ferramenta `calculator` para perguntas sobre pessoas, história ou conceitos não numéricos.
```
🚀 Executando a API

Com o ambiente virtual ativado e o Ollama rodando:
```bash
uvicorn app.main:app --reload
```
A API ficará disponível em:

Interface Web: http://localhost:8000/

Healthcheck: http://localhost:8000/health

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

💻 Interface Web

Este projeto inclui uma interface HTML simples para conversar com o agente sem precisar usar Postman.

Acesse:
```bash
http://localhost:8000/
```
A página permite enviar mensagens e ver as respostas do agente diretamente no navegador.

📡 Endpoint de Chat
POST /chat
Request body (application/json):
```bash
{
  "message": "Quanto é 1234 * 5678?"
}
```

Response body:
```bash
{
  "response": "7021792"
}
```

Exemplo usando curl

Pergunta de cálculo (usa a tool calculator):

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Quanto é 1234 * 5678?\"}"
```

Pergunta de conhecimento geral (NÃO usa tool):

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Quem foi Albert Einstein?\"}"
```

🧠 Lógica do Agente

O agente é configurado em app/agent.py:

Modelo: OllamaModel, configurado via variáveis de ambiente.

Tool registrada: calculator (strands-agents-tools).

Prompt: instrui quando deve e quando não deve usar a tool.

/health e tempos de resposta são registrados nos logs da API.

📝 Observações

O projeto foi estruturado com foco em simplicidade, clareza e boas práticas:

Separação entre configuração, agente, API, schemas e interface web.

Uso de .env e .env.example para configuração do ambiente.

Boas práticas de FastAPI, Pydantic e organização de arquivos.

Interface web minimalista para facilitar testes rápidos.

Healthcheck implementado (/health), padrão em APIs profissionais.