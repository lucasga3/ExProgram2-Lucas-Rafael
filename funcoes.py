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

    novo = (dados_guardados,guardados)

    return novo
