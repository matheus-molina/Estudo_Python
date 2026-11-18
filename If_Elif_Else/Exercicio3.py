
# ============================================================
# 🐍 DESAFIO PYTHON - EXERCÍCIO 03
# ============================================================
#
# TEMA: Estruturas condicionais (if, elif e else)
# NÍVEL: Iniciante
#
# OBJETIVO:
# Criar um sistema que controle a entrada de pessoas
# em um evento com base na idade e no ingresso.
#
# ------------------------------------------------------------
# REGRAS DO PROGRAMA:
# ------------------------------------------------------------
#
# 1. Solicite o nome da pessoa.
#
# 2. Solicite a idade da pessoa.
#
# 3. Pergunte se ela possui ingresso (sim ou não).
#
# 4. Utilize if, elif e else para verificar:
#
#    - Menor de 16 anos:
#      Entrada proibida, mesmo com ingresso.
#
#    - De 16 a 17 anos:
#      Entrada permitida somente com ingresso.
#      Exiba que precisa de um responsável.
#
#    - 18 anos ou mais:
#      Entrada permitida se possuir ingresso.
#
#    - Sem ingresso:
#      Entrada negada.
#
# ------------------------------------------------------------
# EXEMPLO DE EXECUÇÃO:
# ------------------------------------------------------------
#
# Digite seu nome: Matheus
# Digite sua idade: 19
# Possui ingresso? sim
#
# ================================
# Nome: Matheus
# Idade: 19
# Situação: Entrada autorizada!
# ================================
#
# ------------------------------------------------------------
# DESAFIO EXTRA (OPCIONAL):
# ------------------------------------------------------------
#
# 1. Não permitir idades negativas.
#
# 2. Aceitar "SIM", "Sim" e "sim" como resposta.
#
# 3. Se a pessoa digitar algo diferente de
#    "sim" ou "não", mostrar uma mensagem de erro.
#
# 4. Organizar a saída do terminal com separadores.
#
# ============================================================
# ESCREVA SEU CÓDIGO ABAIXO:
# ============================================================

import os

nome = input("Qual é eu nome? \n" \
"Nome: ")

idade = int(input("Qual é a sua idade? \n" \
"Idade: "))

ingresso = input("Você possui ingresso? \n" \
"(S/N): ").upper()

if ingresso != "S" and ingresso != "SIM" and ingresso != "N" and ingresso != "NÃO":
    print("Resposta inválida! Digite S, SIM, N ou NÃO.")
    exit()

os.system("cls")
print("================================")
print("     CONTROLE DE ENTRADA        ")
print("================================")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Ingresso: {ingresso}")
print("================================")
if idade < 0:
    print("Não exite idade negativa!")
    exit()
elif idade < 16:
    if ingresso == "S" or ingresso == "SIM":
        print("Entrada proibida, mesmo com ingresso!")
    else:
        print("Entrada proibida! Você é menor de 16 anos.")
elif idade <= 17 and (ingresso == "S" or ingresso == "SIM"):
    print("Entrada permitida somente com ingresso \n" \
    "Necessario um responsável!") 
elif idade >= 18 and (ingresso == "S" or ingresso == "SIM"):
    print("Entrada permitida!")
else:
    print("Entrada Negada!")