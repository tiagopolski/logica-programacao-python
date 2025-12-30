vetorA = [0,0,0,0,0]
vetorB = [0,0,0,0,0]
vetorC = [0,0,0,0,0]
cont = 0
print('Vetor A:')
while cont<5:
    vetorA[cont] = int(input('Informe valor:'))
    cont = cont + 1 

cont = 0 
print('Vetor B:')
while cont<5:
    vetorB[cont] = int(input('Informe valor:'))
    cont = cont + 1
    
cont=0
while cont<5:
    vetorC[cont] = vetorA[cont] + vetorB[cont]
    cont = cont + 1 

print(vetorB)
print(vetorA)
print(vetorC)