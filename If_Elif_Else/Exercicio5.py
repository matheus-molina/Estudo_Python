
# ============================================================
# 🐍 DESAFIO PYTHON - EXERCÍCIO 05
# ============================================================
#
# TEMA: Estruturas condicionais (if, elif e else)
# NÍVEL: Iniciante
#
# PROJETO: Calculadora de IMC
#
# OBJETIVO:
# Desenvolver um programa que calcule o Índice de
# Massa Corporal (IMC) e apresente uma classificação.
#
# ------------------------------------------------------------
# REGRAS DO PROGRAMA:
# ------------------------------------------------------------
#
# 1. Solicite o nome da pessoa.
#
# 2. Solicite o peso em quilogramas (exemplo: 70,5).
#
# 3. Solicite a altura em metros (exemplo: 1,75).
#
# 4. Calcule o IMC utilizando a fórmula:
#
#    IMC = peso / (altura ** 2)
#
# 5. Utilize if, elif e else para classificar:
#
#    IMC menor que 18.5:
#       Abaixo do peso
#
#    IMC de 18.5 até menos de 25:
#       Peso normal
#
#    IMC de 25 até menos de 30:
#       Sobrepeso
#
#    IMC de 30 até menos de 35:
#       Obesidade grau I
#
#    IMC de 35 até menos de 40:
#       Obesidade grau II
#
#    IMC igual ou maior que 40:
#       Obesidade grau III
#
# ------------------------------------------------------------
# EXEMPLO DE EXECUÇÃO:
# ------------------------------------------------------------
#
# ========================================
#           CALCULADORA DE IMC
# ========================================
#
# Nome: Matheus
# Peso: 70,00 kg
# Altura: 1,75 m
#
# ----------------------------------------
# IMC calculado: 22,86
# Classificação: Peso normal
# ----------------------------------------
#
# ------------------------------------------------------------
# DESAFIOS EXTRAS (OPCIONAIS):
# ------------------------------------------------------------
#
# 1. Aceitar vírgula e ponto ao digitar peso e altura.
#
# 2. Impedir valores negativos ou iguais a zero
#    para peso e altura.
#
# 3. Exibir o IMC com apenas duas casas decimais.
#
# 4. Limpar o terminal antes de mostrar o resultado.
#
# 5. Exibir uma mensagem personalizada com o nome
#    da pessoa e sua classificação.
#
# ============================================================
# ESCREVA SEU CÓDIGO ABAIXO:
# ============================================================

import os

nome = input("Qual é o seu nome? \n" \
"Nome: ")

peso = float(input("Qual é o seu peso? \n" \
"Kg: ").replace(",", "."))

altura = float(input("Qual é a sua altura? \n" \
"Altura em metros: ").replace(",", "."))

if peso <= 0 or altura <= 0:
    print("Informações invalidas!")
    exit()
else: 
    os.system("cls")
    print("========================================")
    print("             CALCULADORA DE IMC         ")
    print("========================================\n")
    print(f"Nome: {nome}")
    print(f"Peso: {peso} Kg".replace(".", ","))
    print(f"Altura: {altura} m".replace(".", ","))
    print("----------------------------------------")
    imc = peso / (altura ** 2) 
    print(f"IMC calculado: {imc: .2f}".replace(".", ","))
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc < 25:
        print("Peso normal.")
    elif imc < 30:
        print("Sobrepeso.")
    elif imc < 35:
        print("Obesidade grau I")
    elif imc < 40:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")

