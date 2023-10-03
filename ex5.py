arquivo1 = open("numPar.txt","r")
arquivo2 = open("numImpar.txt","r")

num_pares = [int(line) for line in arquivo1.readlines()]
num_impares = [int(line) for line in arquivo2.readlines()]

arquivo1.close()
arquivo2.close()


todos_numeros = sorted(num_pares + num_impares)

arquivo_ordenado = open('num.ordenados.txt', 'w')

for numero in todos_numeros:
    arquivo_ordenado.write(str(numero) + '\n')


arquivo_ordenado.close()

