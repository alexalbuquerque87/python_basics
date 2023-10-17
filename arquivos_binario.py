import pickle

x = [1, 2, 3, 4]

a = pickle.dumps(x)
print(a)
#b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04e.'

b = pickle.loads(a)
print(b)
#[1, 2, 3, 4]

#'wb' escreve o arquivo em binário substituindo qualquer informação que já exista no arquivo
#'ab' adiciona informações ao arquivo, sem apagar o que já existe
arq = open('arquivo.pkl', 'wb')
pickle.dump(x, arq)

#'rb' lê o arquivo em binário
arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou)