
# ============================================================
# 🐍 DESAFIO PYTHON - EXERCÍCIO 01
# ============================================================
#
# TEMA: Estruturas condicionais (if, elif e else)
# NÍVEL: Iniciante
#
# OBJETIVO:
# Desenvolver um programa que verifique a situação escolar
# de um aluno com base na nota informada.
#
# ------------------------------------------------------------
# REGRAS DO PROGRAMA:
# ------------------------------------------------------------
#
# 1. Solicite ao usuário que digite sua nota (de 0 a 10).
#
# 2. Utilize if, elif e else para verificar a nota.
#
# 3. Exiba uma mensagem conforme as condições:
#
#    - Nota maior ou igual a 7: APROVADO
#    - Nota maior ou igual a 5 e menor que 7: RECUPERAÇÃO
#    - Nota menor que 5: REPROVADO
#
# ------------------------------------------------------------
# EXEMPLO DE EXECUÇÃO:
# ------------------------------------------------------------
#
# Digite sua nota: 8.5
# Parabéns! Você foi aprovado!
#
# ------------------------------------------------------------
# DESAFIO EXTRA (OPCIONAL):
# ------------------------------------------------------------
#
# Faça o programa identificar notas inválidas.
#
# Exemplo:
# Digite sua nota: 15
# Erro! A nota deve estar entre 0 e 10.
#
# ============================================================
# ESCREVA SEU CÓDIGO ABAIXO:
# ============================================================

print ("Calcule sua média: \n")

nota = float(input("digite sua nota: "))

if nota < 0 or nota > 10:
    print("Erro! A nota deve estar entre 0 e 10!")
elif nota >= 7:
    print("APROVADO !")
elif nota >= 5 and nota < 7:
    print("RECUPERAÇÃO !")
else:
    print("REPROVADO!")