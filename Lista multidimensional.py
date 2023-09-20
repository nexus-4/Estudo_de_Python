matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Numero para [{l}/{c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')

        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
#Soma Numeros pares

print(f'A soma de todos os numeros pares é {spar}')
#Soma da terceira coluna
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos numeros da terceira coluna é {scol}')

#Maior numero da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'o maior numero da linha 2 é {maior}')

