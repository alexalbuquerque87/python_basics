x = [12,13,14,15,16,17,18,19,20,21,22,23,24,25]

x = list(filter(lambda x: x < 18, x))

print(x)

y = [{'nome': 'João', 'idade': 20}, {'nome': 'Pedro', 'idade': 35}]

x = list(filter(lambda y: y['idade'] > 25, y))

print(x)