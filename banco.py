menu ='''
              MENU USUARIO
        S-SAQUE
        D-DEPOSITO
        E-EXTRATO
        q-SAIR      
              
SELECIONE UMA OPÇÃO ACIMA: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
  opcao = input(menu)
  opcao = opcao.upper()
  
  if opcao == 'D':
    deposito = float(input("Insira valor a ser depositado: "))
    if deposito > 0:
      saldo += deposito
      extrato += f"DEPOSITO: R${deposito:.2f}\n"
      print(f"Novo saldo: R${saldo:.2f}\n")
    else:
      print("Valor incorreto")
  
  elif opcao == 'S':
    if numero_saques >= LIMITE_SAQUES:
      print("Limite de saques excedidos")
    else:
      saque = float(input("Insira valor a ser sacado: "))
      if saque > saldo:
        print("Saldo insuficiente")
      else:
        saldo -= saque
        extrato += f"SAQUE: R${saque:.2f}\n"
        print("\nRealizando saque\n")
        print(f"Novo saldo: R${saldo:.2f}")
        numero_saques+=1
    
  elif opcao == 'E':
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}\n')
  elif opcao == 'Q':
    break
  else:
    print('Opção invalida, Por favor selecione novamente')  
