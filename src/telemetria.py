import random
from datetime import datetime

"""Módulo Responsável pela simulação da telemetria do satélite ConnectSat"""

def coletar():
    estados = ["Normal", 
    "Congestionado", 
    "Critico", 
    "Manutenção", 
    "OFFLINE"
    ]

    estado = random.choice(
        estados,
        weights = [50, 30, 10, 5, 5]
    )[0]

    regiao = random.choice([
    "Interior do Amazonas",
    "Sertão Nordestino",
    "Zona Rural do centro-oeste",
    "Zona Rural do sul",
    "Comunidade Ribeirinha"
    ])

    #Estado normal de operação
    if estado == "Normal":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(20, 100),
            "throughput_mbps": random.randint(400, 500),
            "saude_antena": random.randint(80, 100),
            "beam_stearing": "ESTAVEL",
            "temperatura_transponder": random.randint(30, 50),
            "clientes_online": random.randint(10000, 50000),
            "integridade_sinal": random.randint(70, 100),
            "Regiao": regiao
        }

    #Estado de congestionamento
    elif estado == "Congestionado":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(100, 400),
            "throughput_mbps": random.randint(100, 400),
            "saude_antena": random.randint(50, 80),
            "beam_stearing": random.choice(["AJUSTANDO"]),
            "temperatura_transponder": random.randint(50, 70),
            "clientes_online": random.randint(50000, 100000),
            "integridade_sinal": random.randint(55, 70),
            "Regiao": regiao
        }

    #Estado crítico de operação
    elif estado == "Critico":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(400, 800),
            "throughput_mbps": random.randint(5, 100),
            "saude_antena": random.randint(5, 50),
            "beam_stearing": random.choice(["INSTAVEL"]),
            "temperatura_transponder": random.randint(70, 95),
            "clientes_online": random.randint(100000, 200000),
            "integridade_sinal": random.randint(30, 55),
            "Regiao": regiao
        }
    
    #Estado de manutenção
    elif estado == "Manutenção":
        dados = {
            "estado": estado,
            "latencia_ms": random.randint(90, 100),
            "throughput_mbps": random.randint(25, 150),
            "saude_antena": random.randint(40, 70),
            "beam_stearing":"Calibrando!",
            "temperatura_transponder": random.randint(35, 65),
            "clientes_online": random.randint(0, 500),
            "integridade_sinal": random.randint(40, 80),
            "regiao": regiao
        }

    #Estado offline
    else:
        dados = {
            "estado": "OFFLINE",
            "latencia_ms": None,
            "throughput_mbps": None,
            "saude_antena": None,
            "beam_stearing": None,
            "temperatura_transponder": None,
            "clientes_online": None,
            "integridade_sinal": None,
            "regiao": regiao
        }

    
    
    dados["timestamp"] = datetime.now().strftime("%H:%M:%S")
    
    return dados
