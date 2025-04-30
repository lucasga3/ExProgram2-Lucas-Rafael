import random

def rolar_dados(numero):

   lista = []

   for i in range(numero):
       lista.append(random.randint(1,6))
  
   return lista

def guardar_dado (dados_rolados, dados_guardados, guardar):
    novo = []
    guardados = []

    for i in range (len(dados_guardados)):
        guardados.append(dados_guardados[i])
    
    guardados.append(dados_rolados[guardar])
    del dados_rolados[guardar]
    novo = [dados_rolados,guardados]

    return novo

def remover_dado (dados_rolados, dados_guardados, remover):
    rolados = []

    for i in range (len(dados_rolados)):
        rolados.append(dados_rolados[i])

    rolados.append(dados_guardados[remover])
    del dados_guardados[remover]

    novo = [rolados,dados_guardados]
    return novo

def calcula_pontos_regra_simples (faces):
    dicio = {}

    for i in range (1,7):
        dicio[i] = 0
    for dado in faces:
        dicio[dado] += dado

    return dicio

def calcula_pontos_soma (faces):
    resultado = 0
    for i in range(len(faces)):
        resultado += faces[i]
    
    return resultado

def calcula_pontos_sequencia_baixa (faces):
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces:
        return 15
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        return 15
    if 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        return 15
    return 0
