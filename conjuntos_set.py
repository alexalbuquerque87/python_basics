x = [1,1,1,2,2,2,3,4,5]
print(x)
y = set(x) #converte lista x para set / conjunto
print(y)
#set não permite valor repetido

x = {1,2,3,4,5}
print(x)
x = {1,2,2,3,3,3,4,5,5}
print(x)

print("\nPropriedades dos conjuntos")
x = {1,2,3,4,5} 
y = {4,5,6,7,8}
#union
z = x.union(y)
print(f'Union: {z}')
#intersection
z = x.intersection(y)
print(f'intersection: {z}')
#difference
z = x.difference(y) #remove os valores de x que existem em y
print(f'difference: {z}')
z = y.difference(x)
print(f'difference: {z}')
#symmetric_difference
z = x.symmetric_difference(y) #union excluindo os valores semelhantes
print(f'symmetric_difference: {z}')