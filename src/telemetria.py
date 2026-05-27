import random
from datetime import datetime

def coletar():
    estado = random.choice(["Normal", "Congestionado", "Critico", "Manutenção"])


    if estado == "Normal":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(20, 50),
            "throughput_mbps": random.randint(400, 500),
            "saude_antena": random.randint(80, 100),
            "beam_stearing": "ESTAVEL",
            "temperatura_transponder": random.randint(30, 50)
        }

    elif estado == "Congestionado":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(50, 300),
            "throughput_mbps": random.randint(100, 400),
            "saude_antena": random.randint(50, 80),
            "beam_stearing": random.choice(["AJUSTANDO"]),
            "temperatura_transponder": random.randint(50, 70)
        }

    elif estado == "Critico":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(300, 800),
            "throughput_mbps": random.randint(5, 100),
            "saude_antena": random.randint(5, 50),
            "beam_stearing": random.choice(["INSTAVEL"]),
            "temperatura_transponder": random.randint(70, 95)
        }
    
    else:  # Manutenção
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(0),
            "throughput_mbps": random.randint(0),
            "saude_antena": random.randint(0),
            "beam_stearing": random.choice(["MANUTENÇÃO!"]),
            "temperatura_transponder": random.randint(0, 100)
        }

    
    
    dados["timestamp"] = datetime.now().strftime("%H:%M:%S")
    
    return dados
