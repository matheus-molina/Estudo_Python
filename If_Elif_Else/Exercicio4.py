
# ============================================================
# 🐍 DESAFIO PYTHON - EXERCÍCIO 04
# ============================================================
#
# TEMA: Estruturas condicionais (if, elif e else)
# NÍVEL: Iniciante
#
# PROJETO: Simulador de Caixa Eletrônico
#
# OBJETIVO:
# Desenvolver um sistema bancário simples que permita
# realizar saques conforme algumas regras.
#
# ------------------------------------------------------------
# REGRAS DO PROGRAMA:
# ------------------------------------------------------------
#
# 1. O cliente começa com um saldo de R$ 1.000,00.
#
# 2. Solicite o nome do cliente.
#
# 3. Pergunte quanto ele deseja sacar.
#
# 4. Utilize if, elif e else para verificar:
#
#    - Saque menor ou igual a zero:
#      Mostrar "Valor de saque inválido!"
#
#    - Saque maior que R$ 500,00:
#      Mostrar "Limite por saque excedido!"
#
#    - Saque maior que o saldo disponível:
#      Mostrar "Saldo insuficiente!"
#
#    - Caso contrário:
#      Autorizar o saque.
#
# 5. Se o saque for autorizado, calcule o saldo restante.
#
# ------------------------------------------------------------
# EXEMPLO DE EXECUÇÃO:
# ------------------------------------------------------------
#
# ========================================
#           CAIXA ELETRÔNICO
# ========================================
#
# Cliente: Matheus
# Saldo disponível: R$ 1000,00
# Quanto deseja sacar? R$ 250,00
#
# ----------------------------------------
# Saque realizado com sucesso!
# Valor sacado: R$ 250,00
# Saldo restante: R$ 750,00
# ----------------------------------------
#
# ------------------------------------------------------------
# DESAFIOS EXTRAS (OPCIONAIS):
# ------------------------------------------------------------
#
# 1. Aceitar vírgula e ponto nos valores digitados.
#
# 2. Mostrar todos os valores em reais com duas casas
#    decimais e vírgula (exemplo: R$ 750,00).
#
# 3. Limpar o terminal antes de mostrar o resultado.
#
# 4. Impedir que um saque inválido mostre a mensagem
#    de saque realizado com sucesso.
#
# 5. Exibir uma mensagem personalizada com o nome
#    do cliente quando o saque for autorizado.
#
# ============================================================
# ESCREVA SEU CÓDIGO ABAIXO:
# ============================================================

import os 

saldo = float(1000)

nome = input("Qual é o seu nome?\n" \
"Nome: ")

saque = float(input("Quanto vc deseja sacar? \n"
"Saque: ").replace(",", "."))

if saque <= 0:
    os.system("cls")
    print("Valor de saque inválido!")
    exit()
elif saque > 500:
    os.system("cls")
    print("Limite por saque excedido!")
    exit()
elif saque > saldo:
    os.system("cls")
    print("Saldo insuficiente!")
    exit()
else:
    os.system("cls")
    print("========================================")
    print("         CAIXA ELETRÔNICO               ")
    print("========================================\n")
    print(f"Saque altorizado: {nome} !\n")
    saldoRestante = saldo - saque
    print(f"Saque realizado: R$ {saque: .2f}".replace(".", ","))
    print(f"Saldo restante: R$ {saldoRestante: .2f}\n".replace(".", ","))