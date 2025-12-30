matriz = []
idade = -1
for i in range(2):
    lista = []
    for j in range(5):
        lista.append(int(input('Informe idade:')))
        if lista[j] > idade:
            idade = lista[j]
            posLinha = i 
            posColuna = j 
    matriz.append(lista)
print(matriz)
print(f'Maior idade: {idade} na linha {posLinha} e na coluna {posColuna}')