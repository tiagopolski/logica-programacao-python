num = 5
notas = []
validas = 5
soma = 0 

# Leitura das notas e validação dos valores
for i in range(num):
    notas.append(float(input('Informe a nota:')))
    if notas[i] < 0 or notas[i] > 10:
        validas = validas - 1 
    else:
        soma = soma + notas[i]

print(notas) 

# Cálculo da média das notas válidas
if validas > 0:
    print('Media:', soma/validas)

# Ordenação das notas
for j in range(num):
    for i in range(num-1):
        if notas[i] > notas[i + 1]:
            x = notas[i]
            notas[i] = notas[i + 1]
            notas[i + 1] = x 

print(notas)
print(f'Maior 1:{notas[num-1]}')
print(f'Maior 2:{notas[num-2]}')
print(f'Maior 3:{notas[num-3]}')

