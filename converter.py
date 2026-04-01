def main():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    escolha = input("Escolha uma opção (1 ou 2): ").strip()
    
    if escolha == '1':
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")
            
    elif escolha == '2':
        try:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")
            
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()