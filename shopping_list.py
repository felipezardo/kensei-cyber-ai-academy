def main():
    shopping_list = []
    
    while True:
        print("\nMenu da Lista de Compras:")
        print("1. Adicionar item")
        print("2. Ver itens")
        print("3. Remover item")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4): ").strip()
        
        if choice == '1':
            item = input("Digite o item a adicionar: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' adicionado à lista.")
            else:
                print("Item não pode ser vazio.")
        
        elif choice == '2':
            if shopping_list:
                print("\nItens na lista:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("A lista está vazia.")
        
        elif choice == '3':
            if shopping_list:
                print("\nItens na lista:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                index_str = input("Digite o número do item a remover: ").strip()
                try:
                    index = int(index_str) - 1
                    if 0 <= index < len(shopping_list):
                        removed_item = shopping_list.pop(index)
                        print(f"'{removed_item}' removido da lista.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("A lista está vazia.")
        
        elif choice == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()