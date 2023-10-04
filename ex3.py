#Faça um programa que crie um arquivo de texto denominado "arquivo. txt" e 
#permita que o usuário grave diversos caracteres nesse arquivo até que seja digitado o caractere "O" (zero).

arquivo = open("arquivo.txt","w")

while True:
    caracteres = input('escreva aqui (0 para sair): ')
    if caracteres == '0':
        break
    arquivo.write(caracteres + '\n')

arquivo.close()