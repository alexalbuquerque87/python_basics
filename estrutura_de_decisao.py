nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'Aluno aprovado com media {media}')
elif media >=4:
    print(f'Aluno em recuperação com media {media}')
else:
    print(f'Aluno reprovado com media {media}')