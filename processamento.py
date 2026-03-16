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