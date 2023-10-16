nomes = ['João', 'Marcos', 'Pedro']

print(nomes) #['João', 'Marcos', 'Pedro']
print(nomes[1]) #Marcos
print(len(nomes)) #3

nomes[0] = 'Alex'
print(nomes) #['Alex', 'Marcos', 'Pedro']

nomes.append('Maria') #adiciona ao final da lista
print(nomes) #['Alex', 'Marcos', 'Pedro', 'Maria']

#insere no indice 0 sem remover nennhum valor
nomes.insert(0, 'insert 0')
nomes.insert(2, 'insert 2')
nomes.insert(9, 'insert 9')
print(nomes)

#remove último elemento da lista se não for informado index
nomes.pop()
print(nomes)
nomes.pop(2)
nomes.pop(0)
print(nomes)

#remove o primeiro valor encontrado baseado no valor da list
nomes.remove('Alex')
print(nomes)

#informa o index do valor
print(nomes.index('Pedro'))

#sort ordena a lista substituindo-a
numeros = [3, 5, 27, 1, 2, 45, 60, 6, 1.5]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

#sorted ordena sem substituir a lista
numeros = [3, 5, 27, 1, 2, 45, 60, 6, 1.5]
sorted(numeros)
print(numeros)
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
numeros_ordenados_reverso = sorted(numeros,reverse=True)
print(numeros_ordenados_reverso)

#iterando listas
numeros = [3, 5, 27, 1, 2, 45, 60, 6, 1.5]
print('\nforma habitual')
#print o index
for i in range(0, len(numeros)):
    print(i)
print('\n')
#print o valor no index
for i in range(0, len(numeros)):
    print(numeros[i])

print('\nforma pythonica')
for i in numeros: #desta forma não é possível acessar o index
    print(i)
#para acessar o index, é utilizado o enumerate
x = list(enumerate(numeros))
print('\n')
print(x) #(index, valor)

print('\n')
#iterando o enumerate
for i in enumerate(numeros):
    print(i) #cada valor é uma tupla (index=0, valor=1)
    print(i[0]) #index
    print(i[1]) #valor
#lista [] - tupla ()

print('\n')
#descompactando o enumerate
for i,j in enumerate(numeros):
    print(f'index = {i} / valor = {j}')

print('\n')
#lista de listas
idades = [[1,2],[6,7,8],[11]]
for i in range(0, len(idades)):
    for j in range(0, len(idades[i])):
        print(f'Idade em i={i} e j={j} é {idades[i][j]}')

print('\n')
#Receba 10 valores e exiba a soma de todos eles
x = [int(input()) for i in range(0,10)]
soma = 0
for i in x:
    soma += i
print(soma)