menu = """
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} ! \n"
        else:
            print("Valor inválido, tente novamente!")

    elif opcao == "s":
        valor_saque = float(input("Qual valor deseja sacar: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou: você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Operação falhou: o valor do saque excede o limite!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f} ! \n"
            numero_saques += 1
        else:
            print("Operação falhou: valor informado inválido!")

    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
