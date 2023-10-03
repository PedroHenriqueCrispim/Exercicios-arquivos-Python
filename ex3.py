arquivo = open("arquivo.txt","w")

while True:
    caracteres = input('escreva aqui (0 para sair): ')
    if caracteres == '0':
        break
    arquivo.write(caracteres + '\n')

arquivo.close()