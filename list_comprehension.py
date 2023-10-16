#programacao funcional
x = [i for i in range(0, 10)]
print(x)

#feito na forma habitual seria. Resultado é o mesmo
y=[]
for i in range(0, 10):
    y.append(i)
print(y)

print('\n')
a = [1,2,3,4,5]
b = [i*2 for i in y]
print(b)

print('\n')
#c = [input('Digite um nome: ') for i in range(0, 3)]
#print(c)

print('\n')
#d = [[[input() for h in range(0, 2)] for j in range(0,2)] for i in range(0,2)]
#print(d)

print('\n')
e = [i for i in range(0, 10) if i > 4]
print(e)