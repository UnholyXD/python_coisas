sexo = input("qual o sexo? [m/f]").upper()
altura = float(input("Qual a sua altura? "))

if sexo == "M":
    print("Seu peso ideal é", ((72.7*altura) - 58))
else:
    print("Seu peso ideal é", ((62.1*altura) - 44.7))
