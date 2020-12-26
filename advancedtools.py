# list comprehension -> Make operations in every element in one list
# beginner method
x = [1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(i**2)

print(x)
print(y)

# smart tool -> list comprehension
a = [1, 2, 3, 4, 5]
b = [i**2 for i in a]
print("Usando List Comprehension")
print(a)
print(b)

# Using condition
c = [1, 2, 3, 4, 5]
d = [i**2 for i in c]
e = [i**2 for i in c if i%2 == 1]
print(e)

# Enumerate -> Tool for print more than one variable 
# Beginner method

lista = ["abacate", "bola", "cachorro"]
for i in range(len(lista)):
    print(i, lista[i])

# smart tool -> enumerate

lista = ["abacate", "bola", "cachorro"]
for i,nome in enumerate(lista):
    print(i,nome)

# Filter
def pares(i):
    if i%2 == 0:
        return i
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares=filter(pares, lista) # parameters-> function and list
print(list(lista_pares)) # you should converter the filter in order to have a list

# Reduce
from functools import reduce
lista = [1,2,3,5,10,20]
def soma(x,y):
    return x+y
soma = reduce(soma, lista)
print(soma)

# Zip -> Now you can mix lists
lista1=[1,2,3,4,5]
lista2=["abacate", "bola", "cachorro","dinheiro"]
lista3=["R$ 3","R$ 4", "Não tem preço","Não tem preço","Não tem preço"]
lista4=[]
for numero,nome,valor in zip(lista1,lista2,lista3):
    print(numero,nome,valor)
    lista4.append(numero)
    lista4.append(nome)
    lista4.append(valor)
    
print(lista4)

# Map -> You can make some functions work inside a list
def dobro(x):
    return x*2
valor = [1,2,3,4,5]
valor_dobro = map(dobro,valor)
for i in valor_dobro:
    print(i)
valor_dobro = list(valor_dobro)
print(valor_dobro)

#Lambda Functions -> When you want to utilize a function only one time and don't want to waste space

valor = [1,2,3,4,5]
valor_dobro = map(lambda i: i*2,valor)

valor_dobro = list(valor_dobro)
print(valor_dobro)
