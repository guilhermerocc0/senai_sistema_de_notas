def validar_notas(notas):
    if not isinstance(notas, list):
        return False
    if len(notas) == 0:
        return False
    return True