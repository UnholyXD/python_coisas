import random

lista = []
par = []
impar = []

for i in range(20):
    n = random.randint(1,100)
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

lista.sort()
par.sort()
impar.sort()

print("\nLISTA = ", lista)
print("PAR   = ", par)
print("IMPAR = ", impar, "\n")
