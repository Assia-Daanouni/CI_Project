"""Module de calcul simple."""

def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
