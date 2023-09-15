#Indice de massa corporal
def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)
titulo(f'{"IMC CALCULADORA":^55}')
#Recebe informacoes do usuario
peso = float(input('Seu peso(Em KG): '))
altura = float(input('Sua altura(Em metros): '))
#Calculo do indice de massa corporal
def calculo(peso,altura):
    imc = peso / altura ** 2
    if 18.5 <= imc <= 24.99:
        print(f'{imc:.2f} = Peso Normal')
    if 24.99 < imc <= 29.99:
        print(f'{imc:.2f} = Acima do Peso')
    if 29.99 < imc <= 34.99:
        print(f'{imc:.2f} = Obesidade 1. CUIDADO!!!')

calculo(peso,altura)
