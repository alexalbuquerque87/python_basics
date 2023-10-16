def minha_funcao():
    print('sou uma função')

minha_funcao() #sou uma função

def soma_cem_primeiros_numeros():
    soma = 0
    for i in range(0, 101):
        soma += i
    
    print(f'A soma de todos os números de 0 a 100 é: {soma}')

soma_cem_primeiros_numeros() #5050

#funcao com parametros
def soma_numeros(n1, n2):
    print(n1 + n2)

soma_numeros(5, 2) #7
soma_numeros(n2 = 2, n1 = 5) #7

#funcao com argumentos
def argumentos(*args):
    print(args)

argumentos(1,2,3,4,5,6) #(1, 2, 3, 4, 5, 6)

def argumentos_2(n1, n2, *args):
    print(f'n1={n1} n2={n2} args={args}')

argumentos_2(1,2,3,4,5,6) #n1=1 n2=2 args=(3, 4, 5, 6)

def soma_args(*args):
    soma = 0
    for i in args:
        soma += i
    print(soma)

soma_args(1,2,3,4,5,6,7,8) #36

#funcao com kwargs
#forma um dicionário com {key1: value1, key2: value2,...}
def kwargs(**kwargs):
    print(kwargs) #{'teste1': 1, 'teste2': 2, 'teste3': 3}
    print(kwargs['teste1']) #1
    #print(kwargs['teste4']) #erro - teste 4 não foi passado
    x = kwargs.get('teste2')
    print(x) #2
    x = kwargs.get('teste4')
    print(x) #None
    if x:
        print(f'True. x = {x}')
    else:
        print(f'Falso. x = {x}')

kwargs(teste1 = 1, teste2 = 2, teste3 = 3)

#funcao com retorno
def soma_valores(n1, n2):
    soma = n1 + n2
    if soma > 2:
        return soma
    print('Sem retorno / None')

x = soma_valores(1,2) + 1
print(x) #4
y = soma_valores(1,1)
print(y) #None
