def validar_notas(notas):
    if not isinstance(notas, list):
        return False
    if len(notas) == 0:
        return False
    return True

def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)
    return media

def processar_alunos(alunos):

    recuperacao = []
    top_student = ""
    maior_media = 0

    arquivo = open("resultado.txt", "w", encoding="utf-8")

    arquivo.write("RELATORIO DE DESEMPENHO ACADEMICO\n")
    arquivo.write("----------------------------------\n\n")

    for nome, notas in alunos:

        if not validar_notas(notas):
            print(f"Dados inválidos para {nome}")
            continue

        media = calcular_media(notas)

        arquivo.write(f"Aluno: {nome}\n")
        arquivo.write(f"Notas: {notas}\n")
        arquivo.write(f"Média: {media:.2f}\n\n")

        # filtro recuperação
        if media < 7.0:
            recuperacao.append(nome)

        # top student
        if media > maior_media:
            maior_media = media
            top_student = nome

    arquivo.write("----------------------------------\n")

    arquivo.write("Alunos em Recuperação:\n")
    for aluno in recuperacao:
        arquivo.write(f"- {aluno}\n")

    arquivo.write("\nTop Student:\n")
    arquivo.write(f"{top_student} com média {maior_media:.2f}\n")

    arquivo.close()

    print("Relatório gerado em resultado.txt")