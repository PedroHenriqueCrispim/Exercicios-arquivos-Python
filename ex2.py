#Abra o arquivo de texto criado no exercício anterior(ex1).
#Leia o conteúdo do arquivo e mostre o somatório de todos os números contidos no arquivo.

arquivo = open("numeros.txt", "r")

try:
    soma = 0

    for linha in arquivo:
        try:
            numero = int(linha.strip())  # Converte a linha em um número inteiro
            soma += numero
        except ValueError:
            print(f"Ignorando a linha '{linha.strip()}' pois não contém um número inteiro válido.")

    # Exibe a soma
    print(soma)

except FileNotFoundError:
    print("O arquivo não foi encontrado.")
