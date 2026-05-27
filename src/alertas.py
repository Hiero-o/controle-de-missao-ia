from telemetria import dados



def avaliar(dados):
    # Regras de alerta
    alertas = []

    #Temperatura do transponder
    if dados["temperatura_transponder"] > 70:
        alertas.append({
            "tipo": "Temperatura Alta",
            "severidade": "Critico",
            "mensagem": "Temperatura do transponder excedeu o limite seguro.",
            "acao": "Recomenda-se reduzir a potência e iniciar resfriamento."
        })
    elif dados["temperatura_transponder"] >= 50 and dados["temperatura_transponder"] < 70:
        alertas.append({
            "tipo": "Temperatura Elevada",
            "severidade": "Alerta",
            "mensagem": "Temperatura do transporder está elevada, monitorar de perto."
            "acao": "Recomenda-se monitorar de perto e ajustar a operação."
        })

    elif dados["temperatura_antena"] < 50:
        alertas.append({
            "tipo": "Temperatura normal",
            "severidade": "Alerta",
            "mensagem": "Antena operando em temperatura normal."
            "acao": "Nenhuma ação necessária."
        })
    elif dados["temperatura_antena"] == None:
        alertas.append({
            "tipo": "Temperatura Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Temperatura da antena não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de temperatura da antena."
        })



    # Latencia
    if dados["latencia_ms"] > 300:
        alertas.append({
            "tipo": "Latência Alta",
            "severidade": "Critico",
            "mensagem": "Latência de rede está muito alta, indicando possível congestionamento."
            "acao": "Recomenda-se reduzir a carga e investigar a causa."
        })
    elif dados["latencia_ms"] >= 100 and dados["latencia_ms"] <= 300:
        alertas.append({
            "tipo": "Latência Elevada",
            "severidade": "Alerta",
            "mensagem": "Latência de rede está elevada, monitorar de perto."
            "acao": "Recomenda-se monitorar a latência e ajustar a operação conforme necessário."
        })

    elif dados["latencia_ms"] < 100:
        alertas.append({
            "tipo": "Latência Normal",
            "severidade": "Alerta",
            "mensagem": "Latência de rede está dentro dos parâmetros normais."
            "acao": "Nenhuma ação necessária."
        })
    else: dados["latencia_ms"] == None
        alertas.append({
            "tipo": "Latência Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Latência de rede não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de latência."
        })


    # Throughput
    if dados["throughput_mbps"] > 400:
        alertas.append({
            "tipo": "Throughput Alto",
            "severidade": "Alerta",
            "mensagem": "Throughput está alto, indicando boa performance."
            "acao": "Nenhuma ação necessária."
        })
    elif dados["throughput_mbps"] >= 100 and dados["throughput_mbps"] <= 400:
        alertas.append({
            "tipo": "Throughput Moderado",
            "severidade": "Alerta",
            "mensagem": "Throughput está moderado, monitorar de perto."
            "acao": "Recomenda-se monitorar o throughput e ajustar a operação conforme necessário."
        })
    elif dados["throughput_mbps"] < 100:
        alertas.append({
            "tipo": "Throughput Baixo",
            "severidade": "Critico",
            "mensagem": "Throughput está baixo, indicando possível congestionamento ou falha."
            "acao": "Recomenda-se reduzir a carga e investigar a causa."
        })
    else: dados["throughput_mbps"] == None
        alertas.append({
            "tipo": "Throughput Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Throughput não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de throughput."
        })



    # Saude da antena
    if dados["saude_antena"] > 80:
        alertas.append({
            "tipo": "Saúde da Antena Boa",
            "severidade": "Alerta",
            "mensagem": "Saúde da antena está boa, indicando operação estável."
            "acao": "Nenhuma ação necessária."
        })
    elif dados["saude_antena"] >= 50 and dados["saude_antena"] <= 80:
        alertas.append({
            "tipo": "Saúde da Antena Moderada",
            "severidade": "Alerta",
            "mensagem": "Saúde da antena está moderada, monitorar de perto."
            "acao": "Recomenda-se monitorar a saúde da antena e ajustar a operação conforme necessário."
        })
    elif dados["saude_antena"] < 50:
        alertas.append({
            "tipo": "Saúde da Antena Ruim",
            "severidade": "Critico",
            "mensagem": "Saúde da antena está ruim, indicando possível falha ou necessidade de manutenção."
            "acao": "Recomenda-se reduzir a carga e investigar a causa."
        }) 
    else: dados["saude_antena"] == None
        alertas.append({
            "tipo": "Saúde da Antena Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Saúde da antena não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de saúde da antena."
        })
    

    # Beam Steering
    if dados["beam_stearing"] == "ESTAVEL":
        alertas.append({
            "tipo": "Beam Steering Estável",
            "severidade": "Alerta",
            "mensagem": "Beam steering está estável, indicando operação normal."
            "acao": "Nenhuma ação necessária."
        })
    elif dados["beam_stearing"] == "AJUSTANDO":
        alertas.append({
            "tipo": "Beam Steering Ajustando",
            "severidade": "Alerta",
            "mensagem": "Beam steering está ajustando, monitorar de perto."
            "acao": "Recomenda-se monitorar o beam steering e ajustar a operação conforme necessário."
        })
    elif dados["beam_stearing"] == "INSTAVEL":
        alertas.append({
            "tipo": "Beam Steering Instável",
            "severidade": "Critico",
            "mensagem": "Beam steering está instável, indicando possível falha ou interferência."
            "acao": "Recomenda-se reduzir a carga e investigar a causa."
        })
    else: dados["beam_stearing"] == None
        alertas.append({
            "tipo": "Beam Steering Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Beam steering não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de beam steering."
        })


    # Clientes onlines
    if dados["clientes_online"] > 100000:
        alertas.append({
            "tipo": "Número de Clientes Online Alto",
            "severidade": "Alerta",
            "mensagem": "Número de clientes online está alto, monitorar de perto."
            "acao": "Recomenda-se monitorar o número de clientes online e ajustar a operação conforme necessário."
        })
    elif dados["clientes_online"] >= 50000 and dados["clientes_online"] <= 100000:
        alertas.append({
            "tipo": "Número de Clientes Online Moderado",
            "severidade": "Alerta",
            "mensagem": "Número de clientes online está moderado, monitorar de perto."
            "acao": "Recomenda-se monitorar o número de clientes online e ajustar a operação conforme necessário."
        })
    elif dados["clientes_online"] < 50000:
        alertas.append({
            "tipo": "Número de Clientes Online Baixo",
            "severidade": "Alerta",
            "mensagem": "Número de clientes online está baixo, monitorar de perto."
            "acao": "Recomenda-se monitorar o número de clientes online e ajustar a operação conforme necessário."
        })  
    else: dados["clientes_online"] == None
        alertas.append({
            "tipo": "Número de Clientes Online Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Número de clientes online não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de clientes online."
        })


    # Integridade do Sinal
    if dados["integridade_sinal"] > 80:
        alertas.append({
            "tipo": "Integridade do Sinal Boa",
            "severidade": "Alerta",
            "mensagem": "Integridade do sinal está boa, indicando operação estável."
            "acao": "Nenhuma ação necessária."
        })
    elif dados["integridade_sinal"] >= 50 and dados["integridade_sinal"] <= 80:
        alertas.append({
            "tipo": "Integridade do Sinal Moderada",
            "severidade": "Alerta",
            "mensagem": "Integridade do sinal está moderada, monitorar de perto."
            "acao": "Recomenda-se monitorar a integridade do sinal e ajustar a operação conforme necessário."
        })
    elif dados["integridade_sinal"] < 50:
        alertas.append({
            "tipo": "Integridade do Sinal Ruim",
            "severidade": "Critico",
            "mensagem": "Integridade do sinal está ruim, indicando possível falha ou interferência."
            "acao": "Recomenda-se reduzir a carga e investigar a causa."
        })
    else: dados["integridade_sinal"] == None
        alertas.append({
            "tipo": "Integridade do Sinal Desconecatada",
            "severidade": "Alerta",
            "mensagem": "Integridade do sinal não disponível, possível falha de sensor, comunicação ou manutenção."
            "acao": "Recomenda-se verificar o sensor de integridade do sinal."
        })


    return alertas