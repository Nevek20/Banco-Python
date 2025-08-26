# banco python
import json
import os

logins = "dados.json"

# Se existir o 'dados.json', ele carregará
if os.path.exists(logins):
    with open (logins, "r", encoding="utf-8") as f:
        try:
            listar_dados = json.load(f)
        except json.JSONDecodeError:
            listar_dados = []

# O menu para entrar na sua conta do banco
def menu():
    try:
        def tentativa():
            escolha = int(input("Olá, bem vindo ao Banco.\n\n1)Entrar na conta.\n2)Fazer cadastro.\n3)Sair.\n\n"))
            # Entrar na conta
            if escolha == 1:
                login1 = input("Login: ")
                senha1 = input("Senha: ")

                for usuario in listar_dados:
                    if usuario["login"] == login1 and usuario["senha"] == senha1:
                        print(f"\033[32m\nLogin feito com sucesso!!\nBem vindo {usuario['nome']}\33[0m")
                    else:
                        def error():
                            erro = int(input("\33[31m\nUsuário ou senha inválidos.\n\033[0m\n\nDeseja tentar novamente?\n\n1)Sim, gostaria\n2)Não, quero voltar ao menu\n\n"))
                            if erro == 1:
                                tentativa()
                            else:
                                menu()
            # Registrar
            elif escolha == 2:
                login2 = input("Login: ")
                senha2 = input("Senha: ")
                nome2 = input("Nome completo: ")

                # cria um novo registro
                login = {
                    "login": login2,
                    "senha": senha2,
                    "nome": nome2
                }

                # add a lista de dados
                listar_dados.append(login)

                with open ("dados.json", "w", encoding="utf-8") as f:
                    json.dump(listar_dados, f, ensure_ascii=False, indent=4)

                print("\n\033[32mLogin criado com sucesso!!\n\33[0m")
                menu()
            # Sair do app
            elif escolha == 3:
                print("Adeus\n\n")
            else:
                print("Digite um número válido\n")
                menu()
            
    except ValueError:
        print("Por favor, digite o número correto.\n")
        menu()
    tentativa()
menu()