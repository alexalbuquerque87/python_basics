#w write, r read, a append
# arquivo_write = open('pessoas.txt', 'w')

# i=0
# while True:
#     if i > 1:
#         break
#     arquivo_write.write(input('Digite o nome: ') + " " + input('Digite a idade: ') + "\n")
#     i += 1

arquivo_read = open('pessoas.txt', 'r')
resultado = arquivo_read.readlines()

for i in resultado:
    print(i)

x = []
for i in resultado:
    x.append(i.split())

print(x) #[['joao', '20'], ['pedro', '30']]
print(x[1]) #['pedro', '30']
print(x[1][0]) #pedro

#o arquivo precisa ser fechado depois das operações
arquivo_read.close()

#Outra forma. Dessa forma o arquivo é fechado automaticamente
with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)