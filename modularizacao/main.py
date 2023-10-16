#import minha_lib #importa tudo de minha_lib
#from minha_lib import x #importa somente x
#from minha_lib import x, y #importa x e y
#from minha_lib import * #importa tudo
from minha_lib import x as x_importado
from minha_lib import soma_numero
from minha_lib import soma_numero as soma_lib
from minhas_funcoes.outra_lib import multiplica_numero

#import minha_lib
#print(minha_lib.x) #10
#print(minha_lib.y) #20

#from minha_lib import x / x,y / *
#print(x) #10
#print(y) #20

#from minha_lib import x as x_importado
x = 50
print(x) #50
print(x_importado) #10

#from minha_lib import soma_numero
soma = soma_numero(2, 3)
print(soma) #5

#from minha_lib import soma_numero as soma_lib
soma = soma_lib(4, 5)
print(soma) #9

#from minhas_funcoes.outra_lib import multiplica_numero
multiplica = multiplica_numero(2, 3)
print(multiplica) #6