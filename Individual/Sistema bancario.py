import os

def menu():
    quantidade = 0
    while True: 
        os.system("cls")
        print("============Bem vindo ao Sistema Bancário!============\n\t\n\t\t1.Depósito\n\t\t2.Saque\n\t\t3.Extrato\n\t\t4.Sair")
        escolha = int(input("\nOpção: "))
        if escolha == 1:
            quantidade = deposito(quantidade)
            
        elif escolha == 2:
            quantidade = saque(quantidade)
            
        elif escolha == 3:
            extrato(quantidade)

        elif escolha == 4:
            print("Até mais!")
            exit() 
        else:
            print("Digite uma opção válida!")

def deposito(quantidade):
    os.system("cls")
    print("\n\t============Depósito============")
    while True:
        depositar = float(input("\nDigite o valor que deseja depositar: "))
        if depositar < 0:
            print("Encerrando depósitos.")
            break
        
        quantidade = quantidade + depositar
        print(f"\nDepósito de R${depositar:.2f} realizado com sucesso!")
        
        escolha = input("\nDeseja fazer mais algum depósito (S/N)? ").upper()
        if escolha == "N" or escolha == "NÃO" or escolha == "NAO":
            return quantidade
        elif escolha == "S" or escolha == "SIM":
            continue
        else:
            print("Escolha inválida, encerrando o programa.")
            break
    
    return quantidade

def saque(quantidade):
    os.system("cls")
    print("\n\t============Saque============")
    if quantidade <= 0:
        print("\nNão há nenhum valor disponível para o saque! Voltando ao menu.")
        return quantidade
    
    cont = 0
    while cont < 3:
        valor_saque = float(input(f"\nQual valor você deseja sacar? Valor disponível: {quantidade}\n\nResposta: "))
        cont += 1
        if cont == 3:
            print("É possível apenas três vezes para afetuar o saque! Voltando ao menu.")
            return quantidade
        
        quantidade = quantidade - valor_saque
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
        
        escolha = input("Deseja fazer mais algum saque (S/N)? ").upper()
        if escolha == "N" or escolha == "NÃO" or escolha == "NÃO":
            break
        elif escolha == "S" or escolha == "SIM":
            cont = 0  
            continue
        else:
            print("Escolha inválida, encerrando o programa.")
            break
    
    return quantidade

def extrato(quantidade):
    os.system("cls")
    print("\n\t============Extrato============")
    while True:
        print(f"O saldo atual é: R${quantidade:.2f}")
        escolha = input("Deseja voltar ao menu (S/N)? ").upper()
        if escolha == "N" or escolha == "NÃO" or escolha == "NAO":
            print("Programa encerrado.")
            exit()
        elif escolha == "S" or escolha == "SIM":
            return quantidade
        else:
            print("Escolha inválida, encerrando o programa.")
            break

menu()
