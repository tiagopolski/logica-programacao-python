n = int(input('Digite o número de cofres:'))
cofres = []
for i in range(n):
    valor = float(input(f'Digite o valor do cofre {i + 1}: '))
    cofres.append(valor)

total = sum(cofres)

max = cofres.index(max(cofres))
min = cofres.index(min(cofres))

print(f'Valor total de galeôes: {total}')
print(f'Cofre com mais galeões: Cofre {max + 1}')
print(f'Cofre com menos galeôes: Cofre {min + 1}')
