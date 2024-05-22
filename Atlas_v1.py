from drjit import width


menu_operacoes = """

[d] DEPOSITO
[s] SAQUE
[e] EXTRATO
[q] SAIR

==>"""

saldo_atual = 0
limite_diario = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    operacao = input(menu_operacoes)

    if operacao == "d":
        valor = float(input("Valor do depósito desejado: "))

        if valor > 0 :
            saldo_atual += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não foi possível completar a operação")
    elif operacao == "s":
        valor = float(input("Valor do saque desejado: "))
        if  numero_saques > LIMITE_SAQUES or valor > limite_diario or valor > saldo_atual:
            print("Não foi possível realizar a operação")
        elif valor > 0:
            saldo_atual -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 
        else:
            print("Operação falhou")
    elif operacao == "e":
        print("EXTRATO".center(15,"#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_atual:.2f}")
        print("".center(15,"#"))
    elif operacao == "q":
        print("\nSaindo...")
        break
    else:
        print("Operação inválida, tente novamente")