import os

from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "connectsat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '') 
    }
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
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
        return True #trocar para True quando analyze() estiver implementado

    def status_snapshot(self):
        dados = coletar()
        return f"""
        Status da Missão
        Latência: {dados['latencia_ms']} ms
        Throughput: {dados['throughput_mbps']} Mbps
        Saúde da Antena: {dados['saude_antena']}%
        Beam Steering: {dados['beam_stearing']}
        Temperatura do Transponder: {dados['temperatura_transponder']}°C
        Clientes Online: {dados['clientes_online']}
        Integridade do Sinal: {dados['integridade_sinal']}%
        Região: {dados['Regiao']}
        """

    def analyze(self, pergunta_usuario):
        dados = coletar()
        alertas = avaliar(dados)
        prompt = f"""
        Dados atuais da missão:
        {dados}

        Alertas detectados:
        {alertas}
        Pergunta ao operador:
        {pergunta_usuario}
        """
        resposta = llm(
            prompt,
            system=self.system_prompt,
        )

        return resposta
    
     
           