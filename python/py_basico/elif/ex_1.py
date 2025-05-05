# @title Exercicio 2


'''Desenvolva um programa que leia o valor de um produto e a forma de pagamento
a vista em dinheiro = 15% desconto
a vista no cartao = 10% desconto
em 2x no cartao = preço normal
em 3x ou mais no cartao = 20% de juros'''

valor_produto = float(input("Digite o valor do produto: R$ "))

print("\nEscolha a forma de pagamento:")
print("1 - À vista em dinheiro")
print("2 - À vista no cartão")
print("3 - Em 2x no cartão")
print("4 - Em 3x ou mais no cartão")

forma_pagamento = int(input("\nDigite o número correspondente à forma de pagamento: "))

if forma_pagamento == 1:
    desconto = valor_produto * 0.15
    valor_final = valor_produto - desconto
    print(f"Valor final: R$ {valor_final:.2f}")

elif forma_pagamento == 2:
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print(f"Valor final: R$ {valor_final:.2f}")

elif forma_pagamento == 3:
    print(f"Valor final: R$ {valor_produto:.2f}")

else:
    juros = valor_produto * 0.20
    valor_final = valor_produto + juros
    print(f"Valor final: R$ {valor_final:.2f}")
