def main():
    while True:
        nome = input("Digite seu nome (ou 'sair' para encerrar): ").strip()
        
        if nome.lower() == 'sair':
            print("Até logo!")
            break
        
        if not nome:
            print("Nome não pode estar vazio. Tente novamente.")
            continue
        
        print(f"Olá, {nome.upper()}!")

if __name__ == "__main__":
    main()
