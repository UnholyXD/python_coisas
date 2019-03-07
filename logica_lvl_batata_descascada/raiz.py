""""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
 os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

FEITO POR https://powerpython.wordpress.com/2012/03/19/aula-python-16-estrutura-de-decisao/
Somente adaptado
"""
import math


def main():
    a = float(input("Informe o valor de A "))
    if a == 0:
        print("Isso não é uma equação de segundo grau")
    else:
        calculo(a)


def calculo(a):
    b = float(input("Informe o valor de B "))
    c = float(input("Informe o valor de C "))

    delta = (math.pow(b, 2) - (4 * a * c))
    if delta < 0:
        print("delta = ", delta, " a equacao nao possui raizes reais")
    if delta == 0:
        print("delta = ", delta, " a equacao possui uma raiz")
        raiz = ((-1) * b + math.sqrt(delta)) / (2 * a)
        print("raiz da equacao = ", raiz)
    if delta > 0:
        print("delta = ", delta, " a equacao possui duas raizes")
        raiz1 = ((-1) * b + math.sqrt(delta)) / (2 * a)
        raiz2 = ((-1) * b - math.sqrt(delta)) / (2 * a)
        print("raiz1 da equacao = ", raiz1)
        print("raiz2 da equacao = ", raiz2)


main()






