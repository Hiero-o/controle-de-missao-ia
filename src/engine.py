import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TRILHA = "connectsat"

client = Client(
    host="https://ollama.com"
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}

)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    messages = []
    if system:
        messages.append({"role": "user", "content": prompt})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b", messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
           )['message']['content'].strip()
        except Exception as e:
            return f" Erro ao consultar IA: {e}" 

def load_system_prompt():
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente."

class MissionEngine:
    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
    
    def is_ready(self):
        return False #trocar para True quando analyze() estiver implementado

    def status_snapshot(self):
        return " status_snapshot() ainda não implementado"

    def analyze(self, pergunta_usuario):
        #todo: implementar análise da pergunta do usuário e retornar resposta
        # 1. Coletar dados via src.telemetria.coletar()
        # 2. avaliar alertas via src.alertas.avaliar()
        # 3. montar prompt com dados + alertas + pergunta do usuário
        # 4. chamar llm(prompt, system=self.system_prompt)
        # 5. Retornar resposta
        return (
            "   Implementação pendente. \n \n"
            "Olá! A interface CLI está funcionando, mas a lógica\\n"
            "de análise ainda não foi conectada. O grupo precisa:"
            "1. Implementar a coleta de dados em src.telemetria.coletar()\\n"
            "2. Completar src/alertas.py"
            "3. Escrever o system prompt em prompts/system_prompt.md"
            "4. Sobrescrever analyse() em src/engine.py"
        )
    
     
           