vetor = []
qtde = int(input('Informe número de cofres:'))
vetor.append(float(input('Informe valor:')))
maior = vetor[0]
menor = vetor[0]
posMaior = 0
posMenor = 0
soma = vetor[0]
for cont in range(1,qtde):
    vetor.append(float(input('Informe valor:')))
    if vetor[cont] > maior:
        maior = vetor[cont]
        posMaior = cont 
    if vetor[cont] < menor:
        menor = vetor[cont]
        posMenor = cont 
    soma = soma + vetor[cont]
print(vetor)
print(soma)
print('Maior no indice:', posMaior)
print('Menor no indice:', posMenor)
