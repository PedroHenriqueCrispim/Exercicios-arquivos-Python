arquivo1 = open("numPar.txt","w")
arquivo2 = open("numImpar.txt","w")

def par(numeros):
    return numeros % 2 == 0

while True:
    numeros = int(input('Digite um numeroc (0 para sair)'))
    if numeros == 0:
        break
    if par(numeros):
        arquivo1.write(str(numeros) + '\n')
    else:
        arquivo2.write(str(numeros) + '\n')

arquivo1.close()
arquivo2.close()
