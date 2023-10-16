i=0
while i <= 10:
    print(f'i={i}')
    i += 1

print('\n Break loop \n')

j=0
while j <= 10:
    print(f'j={j}')
    if j>= 5:
        print(f'j é igual a {j}. Break')
        break
    j += 1

    
print('\n Continue loop \n')

k=0
while k <= 10:    
    if k % 2 == 1:
        k += 2
        print(f'k é impar e igual a {k}. Continue')
        continue
    print(f'k não é impar e igual a {k}')
    k += 1