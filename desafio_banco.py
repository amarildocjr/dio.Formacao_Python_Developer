menu = """
-------------------------------------
 Escolha o número da opção desejada:

           [1]: Depósito
           [2]: Saque
           [3]: Extrato
           [0]: Sair
-------------------------------------
==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("DEPÓSITO".center(40, "-"))
        valor = float(input("Digite o valor a ser depositado:R$ "))

        if valor <= 0:
            print("Valor digitado inválido. Depósito NÃO efetuado.")
        else:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'
            print("\nDeposito efetuado com Sucesso.")

    elif opcao == "2":
        print("SAQUE".center(40, "-"))
        valor = float(input("Digite o valor a ser sacado:R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque_diario = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque NÃO realizado. Saldo insuficiente.")

        elif excedeu_limite:
            print("Saque NÃO realizado. Você ultrapassou seu limite diario.")

        elif excedeu_saque_diario:
            print("Saque NÃO realizado. Limite de saque diário já foi atingindo.")

        elif valor <= 0:
            print("Saque NÃO efetuado. Valor digitado invalido")

        else:
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque: R$ {valor:.2f}\n'
            print("\nSaque efetuado com sucesso.")
        
    elif opcao == "3":
        print("EXTRATO".center(40, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("=" * 40)

    elif opcao == "0":
        break
    else:
        print("Opção Inválida. Digite novamente: ")

print("Operação finalizada com sucesso. Até mais.")




    


