def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1/2/3): ")
        
        if escolha == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            
        elif escolha == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            
        elif escolha == '3':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
calculadora()
