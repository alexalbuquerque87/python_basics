pessoa = {'nome': 'João', 'idade': '29', 'cep': '123456'}
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cep'])

pessoa['nome'] = 'Marcos'
print(pessoa)

print('\nAppend')
x = {'nomes': [], 'idade': 21}
x['nomes'].append('João')
x['nomes'].append('Caio')
print(x)
print(x['nomes'])
print(x['nomes'][0])

print('\n')
pessoas =   [
                {'nome':'Caio', 'idade':21, 'altura':173},
                {'nome':'João', 'idade':21, 'altura':173},
                {'nome':'Pedro', 'idade':21, 'altura':173}
            ]
print(pessoas)
for pessoa in pessoas:
    print(pessoa)
    print(pessoa['nome'])

print('\nUpdate')
pessoa = {'nome': 'João', 'idade': '29', 'cep': '123456'}
pessoa.update({'cep': '12345678', 'rua': 'Minha rua'})
print(pessoa)
pessoa.update({'cep': '87654321', 'rua': 'Rua minha'})
print(pessoa)

print('\nIterando')
pessoa = {'nome': 'João', 'idade': '29', 'altura': '175'}
print(pessoa.values())#(['João', '29', '175'])
print(pessoa.keys())#(['nome', 'idade', 'altura'])
print(pessoa.items())#([('nome', 'João'), ('idade', '29'), ('altura', '175')])

for i in pessoa.values():
    print(i) #João 29 175

for i in pessoa.keys():
    print(i) #nome idade altura

for i, j in pessoa.items():
    print(f'i = {i} j = {j}') #i = nome j = João i = idade j = 29 i = altura j = 175

print('\n')
#cadastro de n usuários com input
# pessoas = []
# while True:
#     decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
#     if decisao == 2:
#         break

#     nome = input('Digite o nome: ')
#     idade = input('Digite a idade: ')
#     altura = input('Digite a altura: ')
#     pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
#     pessoas.append(pessoa)
#     #tambem poderia passar os inputs direto em pessoa
#     #pessoa = {'nome': input('Digite o nome: '), 'idade': input('Digite a idade: '), 'altura': input('Digite a altura: ')}

# print(pessoas)
