#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random  # Importa a biblioteca para geração de escolhas aleatórias
import string  # Importa constantes de strings (letras, números, pontuação)

def main():
    print("Gerador de Senhas")  # Exibe o título do programa
    
    while True:  # Loop principal para permitir gerar múltiplas senhas
        # Solicitar tamanho da senha
        while True:  # Loop para validação da entrada do tamanho
            try:
                tamanho = int(input("\nDigite o tamanho da senha (mínimo 4): "))  # Lê e converte para inteiro
                if tamanho >= 4:  # Verifica se o tamanho atende ao requisito mínimo
                    break  # Sai do loop de validação
                else:
                    print("Tamanho deve ser pelo menos 4.")  # Mensagem de erro para tamanho insuficiente
            except ValueError:  # Trata o erro caso o usuário digite texto
                print("Por favor, digite um número válido.")
        
        # Solicitar opções de caracteres adicionais
        maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'  # True se digitar 's'
        numeros = input("Incluir números? (s/n): ").strip().lower() == 's'  # True se digitar 's'
        simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'  # True se digitar 's'
        
        # Construir conjunto de caracteres base
        caracteres = string.ascii_lowercase  # Sempre inclui letras minúsculas por padrão
        
        if maiusculas:
            caracteres += string.ascii_uppercase  # Adiciona letras maiúsculas
        if numeros:
            caracteres += string.digits  # Adiciona números
        if simbolos:
            caracteres += string.punctuation  # Adiciona caracteres especiais
        
        # Validação para garantir que a senha use mais do que apenas minúsculas
        if len(caracteres) == len(string.ascii_lowercase):
            print("Erro: Você deve selecionar pelo menos uma opção adicional (maiúsculas, números ou símbolos).")
            continue  # Reinicia o loop principal para o usuário tentar novamente
        
        # Gerar senha aleatória selecionando caracteres do conjunto construído
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        print(f"\nSenha gerada: {senha}")  # Exibe a senha final gerada
        
        # Perguntar se deseja gerar uma nova senha
        gerar_novamente = input("\nDeseja gerar outra senha? (s/n): ").strip().lower()
        if gerar_novamente != 's':
            print("Encerrando o gerador de senhas. Até logo!")
            break  # Encerra o loop principal

if __name__ == "__main__":
    main()