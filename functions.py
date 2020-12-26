def soma(x,y):
    return (x+y)
resultado = soma(2,3)
print(resultado)

#random numers

import random
number = random.randint(1,10)
print(number)

#if you want to fix the number

number = random.seed(1)
print(number)

#random.choice between numbers already in a list

lista = [6,45,9]
numero = random.choice(lista)
print(numero)

#exceptions

a=2
b=3
try:
    print(a/b)
except:
    print("Nao eh permitido divisao por zero")
