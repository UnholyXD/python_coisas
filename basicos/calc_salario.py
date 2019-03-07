horas = float(input("Quantas horas foram trabalhadas? "))
valor = float(input("Qual o valor da hora? "))
salario = horas*valor

print("Salário Bruto R$ ", salario)
print("Valor pago de IR R$ ",(salario*0.11))
print("Valor pago ao INSS R$ ", (salario*0.08))
print("Valor pago ao Sindicato R$ ", (salario*0.05))
print("Salário Líquido ", salario-(salario*0.11)-(salario*0.08)-(salario*0.05))
##salario-(salario*0.24) dessa forma tbm seria possível fazer o calculo final
#- IR (11%) : R$#
#- INSS (8%) : R$#
#- Sindicato ( 5%) : R$#
#= Salário Liquido : R$#
