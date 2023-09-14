from time import sleep
saldo = 0
while True:
    opcao =str(input('''
    [a] Consultar saldo
    [b] Saque
    [c] Deposito
    [d] SAIR
    Sua opcao: '''))
    if opcao in 'aA':
        print(f'Seu \033[1;32mSaldo\033[m é de \033[1;32m{saldo} Reais\033[m')
        if saldo == 0:
            print('\033[31mVoce nao tem saldo na sua conta!!\033[m')

    if opcao in 'Bb':
        qnt_saque = float(input('Quanto vocer quer sacar? '))
        if saldo == 0:
            print('\033[31mVocê não possui saldo suficiente\033[m')
            pass
        else:
            saldo = saldo - qnt_saque
            print('\033[1;32msaque realizado com sucesso!!\033[m')

    if opcao in 'Cc':
        qnt_deposito = float(input('Quanto voce vai depositar? '))
        saldo = qnt_deposito + saldo
        print('\033[1;32mDeposito realizado com sucesso!!\033[m')

    if opcao in 'Dd':
        break

print('\033[31mAutodestruicao acionado...\033[m')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('\033[31mBOOMMMMM!!!!!\033[m')
