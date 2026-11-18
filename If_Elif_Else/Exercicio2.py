
# ============================================================
# EXERCÍCIO 2 - CALCULADORA DE DESCONTOS
# ============================================================
#
# OBJETIVO:
# Desenvolver um sistema que calcule descontos em compras.
#
# REGRAS:
#
# 1. Solicite ao usuário o valor total da compra.
#
# 2. Calcule o desconto conforme as condições:
#
#    - Compra menor que R$ 100: sem desconto
#    - Compra de R$ 100 até R$ 299,99: 5% de desconto
#    - Compra de R$ 300 até R$ 499,99: 10% de desconto
#    - Compra de R$ 500 ou mais: 15% de desconto
#
# 3. Exiba:
#    - Valor original da compra
#    - Porcentagem do desconto
#    - Valor economizado
#    - Valor final com desconto
#
# ============================================================
# EXEMPLO DE EXECUÇÃO:
# ============================================================
#
# Digite o valor da compra: 400
#
# Valor original: R$ 400.00
# Desconto aplicado: 10%
# Você economizou: R$ 40.00
# Valor final: R$ 360.00
#
# ============================================================
# DESAFIO EXTRA (OPCIONAL):
# ============================================================
#
# 1. Não permita compras com valores negativos.
#
# 2. Se a compra for maior ou igual a R$ 1000,
#    conceda um desconto especial de 20%.
#
# ============================================================
# ESCREVA SEU CÓDIGO ABAIXO:
# ============================================================


print("VAMOS CALCULAR SEU DESCONTO:")
gasto = float(input("Quanto vc gastou? \n" \
"R$:").replace(",", "."))

descontoEmReais = 0
descontoEmPorcentagem = 0 

if gasto < 0:
    print("Número negativo não é aceito!")
    exit()
elif gasto < 100:
    print("Valor minpimo para desconto é de 100,00")
    exit()
elif gasto >= 100 and gasto < 300:
    descontoEmPorcentagem = 5
    descontoEmReais = gasto * (5 / 100)
elif gasto >= 300 and gasto < 500:
    descontoEmPorcentagem = 10
    descontoEmReais = gasto * (10 /100)
elif gasto >= 500 and gasto < 1000:
    descontoEmPorcentagem = 15
    descontoEmReais = gasto * (15 / 100)
else:
    descontoEmPorcentagem = 20
    descontoEmReais = gasto * (20 / 100)

valorFinal = gasto - descontoEmReais

economizou = gasto - valorFinal

print(f"====================================== \n" \
f"_Valor original: R$ {f"{gasto:.2f}".replace(".", ",")}\n" \
f"_Desconto aplicado: {descontoEmPorcentagem}%\n" \
f"_Você economizou: R$ {f"{economizou:.2f}".replace(".", ",")}\n" \
f"_Valor final: R$ {f"{valorFinal: .2f}".replace(".", ",")}")