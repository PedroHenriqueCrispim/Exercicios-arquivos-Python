#Um professor armazena em um arquivo de texto uma listagem das notas dos alunos na disciplina,
#onde cada linha contém o nome do aluno e os valores de quatro notas.
#Escreva um programa que leia esse arquivo e calcule a média de cada aluno.

arquivo = open("alunos.txt", "r")

linhas = arquivo.readlines()

notas_alunos = {}

for i in linhas:
    lista = i.strip().split()
    nome = lista[0]
    notas = [float(nota) for nota in lista[-4:]]

    media = sum(notas) / len(notas)

    notas_alunos[nome] = media

for nome, media in notas_alunos.items():
    print(f'{nome}: Média = {media}')

    