def gcd(a: int, b: int) -> int:
    """
    Calcule le plus grand commun diviseur de deux entiers.

    Utilise l'algorithme d'Euclide.

    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.

    Returns
    -------
    int
        Le PGCD de `a` et `b` (toujours positif ou nul).

    Examples
    --------
    >>> gcd(12, 18)
    6
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a