# Kensei Cyber AI Academy

Bem-vindo ao projeto **Kensei Cyber AI Academy**! Este repositório reúne materiais, códigos e exercícios para aprendizado de segurança cibernética com apoio de inteligência artificial.

## 📌 Objetivo

- Consolidar práticas de cibersegurança e IA.
- Implementar ferramentas e desafios de ataque/defesa.
- Aprimorar automações com scripts e padrões de segurança.

## 🚀 Estrutura sugerida do projeto

- `docs/` - Documentação e guias teóricos.
- `src/` - Código-fonte principal (scripts, modelos, automações).
- `examples/` - Exemplos de uso e casos de teste.
- `tools/` - Ferramentas auxiliares de análise ou pentest.

> Observação: A estrutura acima é sugestão; adapte conforme a evolução do projeto.

## 🛠️ Requisitos

- Python 3.11+ (recomenda-se usar virtual environment)
- Node.js (se houver frontend ou ferramentas JS)

## ✔️ Como começar

1. Clone o repositório:
   ```bash
   git clone https://seu-git.git
   cd kensei-cyber-ai-academy
   ```
2. Crie o ambiente virtual (Python):
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   source .venv/bin/activate      # macOS/Linux
   ```
3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Explore as pastas e execute os scripts de exemplo.

## 🧩 Boas práticas

- Mantenha o código modular e documentado.
- Use controle de versão e branches para recursos/bugfix.
- Proteja segredos usando `.env` e `.gitignore`.

## 📝 Contribuição

1. Abra uma issue descrevendo a proposta.
2. Crie uma branch: `feature/novo-componente`.
3. Faça um PR com descrição clara e testes.

## 📄 Licença

Este projeto está licenciado sob MIT License (ou outra, se preferir).

---

> Se quiser, posso ajustar o README para um caso de uso específico (por exemplo, laboratório de análise de malware, sistema de alerta SOC, API de detecção de intrusão etc.).

## Programa de Lista de Compras

Este é um programa simples em Python para gerenciar uma lista de compras, com funcionalidades de adicionar, ver, remover itens e sair.

### Código e Explicação Linha a Linha

```python
def main():
    shopping_list = []  # Inicializa uma lista vazia para armazenar os itens de compras
    
    while True:  # Loop infinito até o usuário escolher sair
        print("\nMenu da Lista de Compras:")  # Exibe o menu de opções
        print("1. Adicionar item")
        print("2. Ver itens")
        print("3. Remover item")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4): ").strip()  # Lê a escolha do usuário e remove espaços extras
        
        if choice == '1':  # Se a escolha for adicionar item
            item = input("Digite o item a adicionar: ").strip()  # Lê o nome do item
            if item:  # Verifica se o item não está vazio
                shopping_list.append(item)  # Adiciona o item à lista
                print(f"'{item}' adicionado à lista.")  # Confirma a adição
            else:
                print("Item não pode ser vazio.")  # Mensagem de erro se vazio
        
        elif choice == '2':  # Se a escolha for ver itens
            if shopping_list:  # Se a lista não estiver vazia
                print("\nItens na lista:")
                for i, item in enumerate(shopping_list, 1):  # Enumera os itens a partir de 1
                    print(f"{i}. {item}")  # Exibe cada item numerado
            else:
                print("A lista está vazia.")  # Mensagem se a lista estiver vazia
        
        elif choice == '3':  # Se a escolha for remover item
            if shopping_list:  # Se a lista não estiver vazia
                print("\nItens na lista:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")  # Mostra a lista numerada
                index_str = input("Digite o número do item a remover: ").strip()  # Lê o número do item
                try:
                    index = int(index_str) - 1  # Converte para inteiro e ajusta para índice 0-based
                    if 0 <= index < len(shopping_list):  # Verifica se o índice é válido
                        removed_item = shopping_list.pop(index)  # Remove o item e o armazena
                        print(f"'{removed_item}' removido da lista.")  # Confirma a remoção
                    else:
                        print("Número inválido.")  # Erro se o número estiver fora do range
                except ValueError:  # Se a entrada não for um número
                    print("Por favor, digite um número válido.")
            else:
                print("A lista está vazia.")  # Mensagem se a lista estiver vazia
        
        elif choice == '4':  # Se a escolha for sair
            print("Saindo...")  # Mensagem de saída
            break  # Sai do loop while
        
        else:  # Se a escolha for inválida
            print("Opção inválida. Tente novamente.")  # Mensagem de erro

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal
```