def func(n):
    """
    Incrémente un nombre donné de 1.

    Args:
        n (int): Un nombre entier.

    Returns:
        int: Le résultat de n + 1.
    """
    return n + 1

def test_answer():
    """
    Teste la fonction func pour s'assurer qu'elle retourne la valeur attendue.

    Le test vérifie que func(3) retourne bien 4. Ce test utilise une assertion pour
    valider le comportement attendu de la fonction.
    """
    assert func(3) == 4