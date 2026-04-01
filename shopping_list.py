def main():
    shopping_list = []  # Inicializa uma lista vazia para armazenar os itens de compras
    
    while True:  # Loop infinito para manter o programa rodando até o usuário decidir sair
        print("\n--- Menu da Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Ver itens")
        print("3. Remover item")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4): ").strip()  # Lê a escolha removendo espaços extras
        
        if choice == '1':  # Adicionar item
            item = input("Digite o item a adicionar: ").strip()  # Lê o nome do item
            if item:  # Verifica se a string não está vazia
                shopping_list.append(item)  # Adiciona ao final da lista
                print(f"✅ '{item}' adicionado à lista.")
            else:
                print("❌ Erro: O item não pode ser vazio.")
        
        elif choice == '2':  # Ver itens
            if shopping_list:  # Verifica se há itens na lista (lista não vazia)
                print("\n📋 Itens na lista:")
                for i, item in enumerate(shopping_list, 1):  # Enumera começando do 1
                    print(f"  {i}. {item}")
            else:
                print("📭 A lista está vazia.")
        
        elif choice == '3':  # Remover item
            if shopping_list:  # Só permite remover se houver algo na lista
                print("\n📋 Itens na lista:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"  {i}. {item}")
                    
                index_str = input("Digite o número do item a remover: ").strip()  
                try:
                    index = int(index_str) - 1  # Converte para inteiro e ajusta para índice 0-based
                    if 0 <= index < len(shopping_list):  # Verifica se o índice existe na lista
                        removed_item = shopping_list.pop(index)  # Remove e retorna o item
                        print(f"🗑️ '{removed_item}' removido da lista.")
                    else:
                        print("❌ Erro: Número de item inválido.")
                except ValueError:  # Captura o erro se o usuário digitar letras em vez de números
                    print("❌ Erro: Por favor, digite um número válido.")
            else:
                print("📭 A lista está vazia. Não há o que remover.")
        
        elif choice == '4':  # Sair do programa
            print("👋 Saindo do gerenciador de lista. Até logo!")
            break  # Interrompe o loop principal, encerrando o script
        
        else:  # Tratamento para opções fora de 1 a 4
            print("⚠️ Opção inválida. Por favor, escolha um número de 1 a 4.")

if __name__ == "__main__":  # Garante que main() só rode se o arquivo for executado diretamente
    main()