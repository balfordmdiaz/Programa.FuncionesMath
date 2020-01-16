def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    try:
        return n1 / n2
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion Incorrecta"