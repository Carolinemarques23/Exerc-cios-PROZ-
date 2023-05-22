def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        operacao = int(input("Digite o número para a operação correspondente: "))
        
        if operacao == 0:
            print("Encerrando o programa...")
            break
        
        elif operacao < 1 or operacao > 4:
            print("Essa opção não existe.\n")
            continue
        
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        
        if operacao == 1:
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
            
        elif operacao == 2:
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
            
        elif operacao == 3:
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
            
        elif operacao == 4:
            if num2 == 0:
                print("Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
        
        print()  # Linha em branco para separar as operações
        
calculadora()
