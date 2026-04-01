#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string

def main():
    print("Gerador de Senhas")
    
    # Solicitar tamanho
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
            if tamanho >= 4:
                break
            else:
                print("Tamanho deve ser pelo menos 4.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Solicitar opções
    maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'
    
    # Construir conjunto de caracteres
    caracteres = string.ascii_lowercase  # Sempre inclui minúsculas
    if maiusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    if len(caracteres) == len(string.ascii_lowercase):
        print("Erro: Você deve selecionar pelo menos uma opção adicional (maiúsculas, números ou símbolos).")
        return
    
    # Gerar senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    main()