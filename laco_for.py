for i in range(0, 5):
    print(i) #0,1,2,3,4

print('-----')

#step
for i in range(0, 20, 2):
    print(i) #prints 0 to 20 with step 2

print('-----')

x = [2 , 7, 'x', 'z', 45]
for i in x:
    print(i)

print('-----')

x = 'Any string'
for i in x:
    print(i)

print('-----')
#Mostra a tabuada completa de todos os números entre 1 e 10
for i in range(1, 11):
    print(f'==========[TABUADA {i}]==========')
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
print('-----')