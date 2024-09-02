saldo = 0.00
extrato_geral = ""
quant_saque = 0

def menu(): #Função de Menu
    while True:
        print("""BANCO SAMUKAS
OPERAÇÔES:
[1] Sacar
[2] Depositar
[3] Visualizar extrato
[0] Sair""")
        opção = int(input("Qual o número da operação que você deseja realizar: ")) #Input para verificar qual opeção o cliente deseja realizar
        if opção == 1:
            sacar()
        elif opção == 2:
            depositar()
        elif opção == 3:
            extrato()
        elif opção == 0:
            print ("Obrigado por ser nosso clinte.")
            break
        else:
            print("Opção invalida tente novamente.")

def sacar(): #Função de sacar
    global saldo, extrato_geral, quant_saque
    while True:
        saque = float(input("Qual valor você deseja sacar: ")) #Input para o valor do saque
        if saque < saldo: 
            if saque <= 500.00 and quant_saque < 3 and saque > 0:
                saldo -= saque
                print(f"Operação concluida sou saldo:\n\033[34mSALDO{saldo:.>27.2f}\033[m")
                quant_saque += 1
                saque_str =  str(f"{saque:.2f}")
                extrato_geral += (f"\033[31mSAQUE{saque_str:.>27}\033[m\n")
                break
            elif saque > 500.00:
                print("Seu limite de saque é R$ 500.00.\nTente outro valor")
            elif quant_saque >= 3:
                print("Sua conta só permite 3 saques por dia.")
                break
            elif saque < 0: 
                print("O sistema não permite valor negativos.\nTente outro valor.")
            else:
                print("Valor invalido tenta novamente.")
        if saldo == 0 or saque > saldo:
            print("Você não tem saldo para realizar essa operação.")
            break

def depositar(): #Função de depósito
    global saldo, extrato_geral
    while True:
        depositado = float(input("Qual valor deseja depósitar: ")) #Input para o valor do depósito
        if depositado < 0:
            print("O sistema não permite valor negativos.\nTente outro valor")
        else:
            saldo += depositado
            print(f"Operação concluida sou saldo:\n\033[34mSALDO{saldo:.>27.2f}\033[m")
            depositado_str = str(f"{depositado:.2f}")
            extrato_geral += (f"\033[32mDEPOSITO{depositado_str:.>24}\033[m\n")
            break
    
def extrato (): #Função de extrato
    saldo_str = str(f"{saldo:.2f}")
    print(f"EXTRATO \n{extrato_geral}\033[34mSALDO{saldo_str:.>27}\033[m")

menu()