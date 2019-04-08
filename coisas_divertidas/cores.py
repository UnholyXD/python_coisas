""""
Código resultado de um desafio feito por mim para um amigo
Vlw W

"""


rnd_str = input("Digite um texto qualquer: ")
target = input('Digite o caractere para destacar: ')
print("".join(str('\033[31m'+letter+'\033[0m' if letter == target else letter) for letter in rnd_str))