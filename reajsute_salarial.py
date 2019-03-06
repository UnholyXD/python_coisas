""""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Qual o salário? "))

if salario <= 280:
    print("Salário antes do reajuste de 20% era de R$ {:.2f}".format(salario))
    print("O aumento foi de R$ {:.2f}".format(salario*.2))
    print("Sendo assim o novo valor do salário é R$ {:.2f}".format(salario + salario * .2))

elif salario > 280 and salario <= 700:
    print("Salário antes do reajuste de 15% era de R$ {:.2f}".format(salario))
    print("O aumento foi de R$ {:.2f}".format(salario*.15))
    print("Sendo assim o novo valor do salário é R$ {:.2f}".format(salario + salario * .15))

elif salario > 700 and salario <= 1500:
    print("Salário antes do reajuste de 10% era de R$ {:.2f}".format(salario))
    print("O aumento foi de R$ {:.2f}".format(salario*.1))
    print("Sendo assim o novo valor do salário é R$ {:.2f}".format(salario + salario * .1))

else:
    print("Salário antes do reajuste de 5% era de R$ {:.2f}".format(salario))
    print("O aumento foi de R$ {:.2f}".format(salario*.05))
    print("Sendo assim o novo valor do salário é R$ {:.2f}".format((salario + salario * .05)))
