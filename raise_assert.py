#força uma mensagem de erro
#raise "ocorreu erro"

#raise ValueError("erro de valor")

#raise ZeroDivisionError("erro dividir por zero")

#assert
x = -2
assert x > 0, "ocorreu erro"
print (x)

#exemplo prático
#função que soma números positivos somente.
#caso seja digitado um número negativo, ocorre erro
def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("n1 e n2 não podem ser negativos")
    return n1 + n2

print(soma(2, -2)) #ValueError: n1 e n2 não podem ser negativos

