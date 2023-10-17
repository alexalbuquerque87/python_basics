x = [i for i in range(12,26)] #[12,13,...,25]
print(x)

#Substitui todos elementos de x por 10
y = list(map(lambda x: 10, x))

print(y)
#[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

z = list(map(lambda x: 10 if x < 18 else(x), x))

print(z)
#[10, 10, 10, 10, 10, 10, 18, 19, 20, 21, 22, 23, 24, 25]

p = [{'nome': 'João', 'idade': 20}, {'nome': 'Pedro', 'idade': 30}]

w = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor que 30 anos'} if x['idade'] < 30 else(x), p))

print(w)
#[{'nome': 'João', 'idade': 'menor que 30 anos'}, {'nome': 'Pedro', 'idade': 30}]