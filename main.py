# banco python
import json
import os
from datetime import datetime

logins = "dados.json"

# Se existir o 'dados.json', ele carregará
if os.path.exists(logins):
    with open (logins, "r", encoding="utf-8") as f:
        try:
            listar_dados = json.load(f)
        except json.JSONDecodeError:
            listar_dados = []

# Limpa o terminal dps de dar algum comando
def pano():
    os.system('cls' if os.name == 'nt' else 'clear')

# O menu para entrar na sua conta do banco
def menu():
    try:
        def tentativa():
            escolha = int(input("Olá, bem vindo ao Banco.\n\n1)Entrar na conta.\n2)Fazer cadastro.\n3)Sair.\n\nDigite: "))
            # Entrar na conta
            if escolha == 1:
                login1 = input("\nLogin: ")
                senha1 = input("Senha: ")

                for usuario in listar_dados:
                    if usuario["login"] == login1 and usuario["senha"] == senha1:
                        print(f"\033[32m\nLogin feito com sucesso!!\n\33[0m")
                        pano()
                        conta(usuario)
                    else:
                        def error():
                            erro = int(input("\33[31m\nUsuário ou senha inválidos.\n\033[0m\n\nDeseja tentar novamente?\n\n1)Sim, gostaria\n2)Não, quero voltar ao menu\n\n"))
                            if erro == 1:
                                tentativa()
                                pano()
                            else:
                                pano()
                                menu()
            # Registrar
            elif escolha == 2:
                login2 = input("Login: ")
                senha2 = input("Senha: ")
                nome2 = input("Nome completo: ")
                data2 = input("(digite: **/**/****) Data de nascimento: ")
                email2 = input("Email: ")

                # cria um novo registro
                login = {
                    "login": login2,
                    "senha": senha2,
                    "nome": nome2,
                    "data": data2,
                    "email": email2
                }

                # add a lista de dados
                listar_dados.append(login)

                with open ("dados.json", "w", encoding="utf-8") as f:
                    json.dump(listar_dados, f, ensure_ascii=False, indent=4)

                print("\n\033[32mLogin criado com sucesso!!\n\33[0m")
                pano()
                menu()
            # Sair do app
            elif escolha == 3:
                print("Adeus\n\n")
            else:
                print("Digite um número válido\n")
                pano()
                menu()
            
    except ValueError:
        print("Por favor, digite o número correto.\n")
        pano()
        menu()
    tentativa()

def extrato(usuario):
    if not usuario['historico']:
        print("\nNão há movimentação no seu banco ainda.")
    else:
        for t in usuario['historico']:
            print(f"{t['data']} - {t['tipo'].capitalize()}: R$ {t['valor']:.2f}")
    print(f"\nSaldo atual: R$ {usuario['saldo']:.2f}\n")

def conta(usuario):
    escolha2 = int(input(f"\033[32mBem-vindo de volta, sr {usuario['nome']}.\33[0m\n\n1)Extrato bancário.\n2)Sacar.\n3)Depositar.\n4)Transferir.\n5)Histórico.\n6)Mudar senha.\n7)Bloquear conta.\n\n8)Sair.\n\nDigite: "))
    if escolha2 == 1:
        extrato(usuario)
    elif escolha2 == 2:
        def saldo(usuario):
            if not usuario['saldo']:
                print(f"\nSaldo atual: R$ {usuario['saldo']:.2f}\n")
            else:
                print(f"\nSaldo atual: R$ {usuario['saldo']:.2f}\n")
menu()