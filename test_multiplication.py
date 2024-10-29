def func(n):
    """
    Multiplie un nombre donné par 2.
 
    Args:
        n (int): Un nombre entier.
 
    Returns:
        int: Le résultat de n * 2.
    """
    return n * 2
 
def test_multiply():
    """
    Teste la fonction func pour s'assurer qu'elle retourne le double du nombre donné.
 
    Le test vérifie les cas suivants :
    - func(3) doit retourner 6
    - func(0) doit retourner 0
    - func(-2) doit retourner -4
    - func(10) doit retourner 20
    Ces assertions couvrent des valeurs positives, négatives et nulles.
    """
    assert func(3) == 6
    assert func(0) == 0
    assert func(-2) == -4
    assert func(10) == 20