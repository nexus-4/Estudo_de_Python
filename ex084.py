lista = []
dado = []
count = maior = menor = 0
while True:
    nome = str(input('Nome: '))
    count += 1
    peso = int(input('Peso: '))
    dado.append(nome)
    dado.append(peso)
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    r = str(input('Quer continuar? S/N : '))
    if r in "Nn":
        break

print(f'Foram cadastradas {count} pessoas na lista')

print(f'Maior peso foi de {maior} para ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'Menor peso foi de {menor} para ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()



