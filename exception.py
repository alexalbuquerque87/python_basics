n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

try:
    print(n1/n2)
except:
    print('Ocorreu erro')
finally: #não é obrigatório no try. Sempre é executado
    print('finally')

print('\n')
#tratando erro específico
try:
    n3 = int(input('Digite um número: '))
    print(5/n3)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0')

#capturando qualquer erro
except Exception as e:
    print(f'erro interno do sistema {e}')
