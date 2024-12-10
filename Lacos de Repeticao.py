salario_atual = float(input("Digite o salário atual: "))

if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

inflacao = 3.8
valor_inflacao = novo_salario * (inflacao / 100)
aumento_real = valor_aumento - valor_inflacao

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
print(f"Valor do aumento real, descontada a inflação: R$ {aumento_real:.2f}")
