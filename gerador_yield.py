#pip install pympler
from pympler.asizeof import asizeof

#imprime o tamanho que o valor ocupa em memória em bits
print(asizeof(5)) #32

def gerador():
    yield 1
    yield 2
    yield 3

x = gerador()

print(next(x))#1
print(next(x))#2
print(next(x))#3
#print(next(x))#erro

def dobro_yield(lista):
    for i in lista:
        yield i*2

x = dobro_yield(range(0, 100))
print(asizeof(x))#496
print(next(x))
print(next(x))

def dobro(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i*2)
    return lista_2

y = dobro(range(0, 100))
print(asizeof(y))#405176
print(y)
