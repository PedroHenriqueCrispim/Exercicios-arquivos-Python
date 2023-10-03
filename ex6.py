arquivo = open("alunos.txt", "r")

linhas = arquivo.readlines()

notas_alunos = {}

for i in linhas:
    lista = i.strip().split()
    nome = lista[0]
    notas = [float(nota) for nota in lista[1:]]

    media = sum(notas) / len(notas)

    notas_alunos[nome] = media

for nome, media in notas_alunos.items():
    print(f'{nome}: Média = {media}')