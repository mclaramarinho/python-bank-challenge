import time

saldo = 0
SAQUES_DIARIOS = 3
LIMITE_POR_SAQUE = 500
cont_saldos = 0
lista_operacoes = []

def deposito (valor):
    global saldo
    print(f"Depositando R${valor}...")
    saldo += valor
    lista_operacoes.append(valor)
    time.sleep(2)
    print("SALDO ATUAL: R$%.2f" % saldo)

def saque (valor):
    global saldo, cont_saldos
    print("Sacando...")
    saldo -= valor
    cont_saldos+=1
    lista_operacoes.append(valor * -1.0)
    time.sleep(2)
    print("SALDO ATUAL: R$%.2f" % saldo)

def extrato ():
    global saldo, lista_operacoes
    print("Imprimindo...")
    time.sleep(3)
    print("EXTRATO".center(7, " "))
    for x in range (0, len(lista_operacoes)):
        print(f"#{x}\tR${float(lista_operacoes[x])}")
        time.sleep(2)
    print(f"\nSALDO ATUAL: R$%.2f" % saldo)

def bank ():

    while True:

        op = int(input("""
    Insira a operação que deseja:
        0 - Encerrar
        1 - Depositar
        2 - Sacar
        3 - Extrato
    """))
        
        if (op == 0):
            print("Obrigado por ser nosso cliente! Até a próxima!")
            break
        elif(op == 1):
            while True:
                valor = float(input("Insira o valor que deseja depositar: R$"))
                if(valor > 0):
                    deposito(valor)
                    break
                else:
                    print("O valor depositado deve ser maior que R$0.00")
        elif(op == 2):
            while True:
                global saldo, cont_saldos
                if(cont_saldos == 3):
                    print(f"Você pode realizar apenar {SAQUES_DIARIOS} por dia. Volte amanha!")
                    break
                else:
                    valor = float(input("Insira o valor que deseja sacar: R$"))
                    if(valor <= saldo):
                        if(valor <= 500):
                                saque(valor)
                                break
                        else:
                            print(f"Cada saque tem um limite de {LIMITE_POR_SAQUE}")
                    else:
                        print(f"O valor sacado deve ser menor ou igual ao saldo de R${saldo}")
        elif (op == 3):
            extrato()

bank()