#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    perguntas = [
        {
            "pergunta": "O que é phishing?",
            "opcoes": ["A) Um tipo de malware", "B) Uma técnica de engenharia social para roubar dados", "C) Um firewall avançado"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é a principal função de um firewall?",
            "opcoes": ["A) Criptografar dados", "B) Bloquear acessos não autorizados à rede", "C) Detectar vírus"],
            "resposta": "B"
        },
        {
            "pergunta": "O que significa a sigla VPN?",
            "opcoes": ["A) Virtual Private Network", "B) Virus Protection Network", "C) Very Personal Network"],
            "resposta": "A"
        },
        {
            "pergunta": "Qual é um exemplo de senha forte?",
            "opcoes": ["A) 123456", "B) password", "C) P@ssw0rd!2023"],
            "resposta": "C"
        },
        {
            "pergunta": "O que é ransomware?",
            "opcoes": ["A) Um tipo de antivírus", "B) Malware que criptografa arquivos e exige resgate", "C) Um software de backup"],
            "resposta": "B"
        }
    ]

    pontuacao = 0

    print("Quiz de Cibersegurança")
    print("Responda com A, B ou C.\n")

    for i, p in enumerate(perguntas, 1):
        print(f"Pergunta {i}: {p['pergunta']}")
        for opcao in p['opcoes']:
            print(opcao)
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == p['resposta']:
            pontuacao += 1
            print("Correto!\n")
        else:
            print(f"Incorreto. A resposta correta é {p['resposta']}.\n")

    print(f"Sua pontuação: {pontuacao}/5")
    if pontuacao >= 3:
        print("Parabéns! Você passou.")
    else:
        print("Você não passou. Tente novamente.")

if __name__ == "__main__":
    main()