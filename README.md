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

## 🧰 Scripts e Ferramentas Disponíveis

Nossos scripts focam na construção de uma base sólida de Python, aplicando conceitos fundamentais como modularização (`def main()`), laços de repetição amigáveis (`while True`), validação de dados e tratamento de exceções (`try/except`).

- **`cyber_quiz.py`**: Um quiz interativo de cibersegurança. Valida entradas estritamente (A, B ou C), possui contagem dinâmica de pontuação e permite jogar múltiplas vezes sem reiniciar o script.
- **`password_generator.py`**: Gerador de senhas customizáveis e seguras. O usuário define o tamanho e os conjuntos de caracteres (maiúsculas, números, símbolos), com validação para garantir a criação de senhas fortes.
- **`shopping_list.py`**: Gerenciador de lista de compras via terminal com uma interface aprimorada (uso de emojis). Evita falhas (crashes) se o usuário digitar letras ao invés de números na hora de remover itens.
- **`converter.py`**: Conversor bidirecional de temperaturas (Celsius ↔ Fahrenheit). Completamente à prova de erros de digitação (letras no lugar de números).
- **`ola.py`**: Script introdutório de saudação em loop, que ensina como lidar com entradas vazias e formatação de strings (`f-strings`).

### 💡 O que você aprenderá explorando os códigos?
- Implementação da estrutura `if __name__ == "__main__":`.
- Manipulação segura de listas e índices em Python.
- Interação contínua com o usuário protegendo o programa contra quebras (crashes).

##  Boas práticas

- Mantenha o código modular e documentado.
- Use controle de versão e branches para recursos/bugfix.
- Proteja segredos usando `.env` e `.gitignore`.

## 📝 Contribuição

1. Abra uma issue descrevendo a proposta.
2. Crie uma branch: `feature/novo-componente`.
3. Faça um PR com descrição clara e testes.

## 📄 Licença

Este projeto está licenciado sob MIT License (ou outra, se preferir).