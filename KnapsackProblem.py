# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:15:06 2019
knapsack problem
@author: lsilv
"""
# Yield and weight x = yield / weight || rendimento e peso  x= rendimento/peso
# Take the file and remove blank lines || Pega o aquivo, retirando as linhas em branco
with open('mochila.txt', 'r') as f:
    arquivo = [linha.strip() for linha in f if linha.strip()]   
 
    
#Separates the number of objects and capacity by transforming into int; and pulling out of the vector || Separa o numero de objetos e a capacidade tarnsformando em int; e retirando do vetor
objetos = int(arquivo[0])
capacidade = int(arquivo[1])
capacidadeOcupada = capacidade
del(arquivo[0],arquivo[0])
profit = []
profitAux = []
objetoRendimento = []
objetoPeso = []
i=0


rendimento = 0



# Transforming values ​​into int and separating weight yield and calculating profit || transformando os valores em int e separando rendimento de peso e calcualndo profit
for a in arquivo:
    profitAux.append(a.split())
    objetoRendimento.append(int(profitAux[i][0]))
    objetoPeso.append(int(profitAux[i][1]))
    profit.append(int(profitAux[i][0])/int(profitAux[i][1]))
    i = i + 1
    
profitAux = []
i=0

# Complete the backpack || completar a mochila 
    
posicao = [(n, profit[n]) for n, x in enumerate(profit) if x==max(profit)]
objetoPeso[posicao[0][0]]


while(capacidadeOcupada > 0):
    posicao = [(n, profit[n]) for n, x in enumerate(profit) if x==max(profit)]
    if(capacidadeOcupada >= objetoPeso[posicao[0][0]]):
        rendimento = rendimento + objetoRendimento[posicao[0][0]]
        capacidadeOcupada = capacidadeOcupada - objetoPeso[posicao[0][0]]
        del(objetoRendimento[posicao[0][0]], objetoPeso[posicao[0][0]],  profit[posicao[0][0]])
        
    posicao = [(n, profit[n]) for n, x in enumerate(profit) if x==max(profit)]    
    if(capacidadeOcupada < objetoPeso[posicao[0][0]]):
        aux = capacidadeOcupada * profit[posicao[0][0]]
        rendimento = rendimento + aux
        capacidadeOcupada = capacidadeOcupada - capacidadeOcupada

print('The performance of the knapsack : {}'.format(rendimento))
