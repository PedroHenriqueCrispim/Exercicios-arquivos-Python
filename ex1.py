#Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada linha).

arquivo = open("numeros.txt", "w")

numbers = []
for i in range(10):
    try:
        num = int(input("Digite o número inteiro: "))
        numbers.append(num)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

for num in numbers:
    arquivo.write(str(num) + "\n")

arquivo.close()