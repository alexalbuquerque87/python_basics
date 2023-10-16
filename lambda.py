#programação funcional
x = lambda: print('ola')

print(type(x)) #<class 'function'>

print(x) #<function <lambda> at 0x00000190DD4C04A0>

print(x()) #ola None

x() #ola

y = lambda: 10

y() #não mostra nada

z = lambda nome, idade: print(f'Nome: {nome} Idade: {idade}')

z('João', 20)

w = lambda *numero: print(numero)

w(10, 20, 30)