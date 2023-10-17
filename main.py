def trouver_min(val: int) -> None:
    """
    Permet de trouver le minimum entre deux valeurs
    :param val: la valeur qu'on doit retourner au minimum
    :return: rien
    """
    global val_min
    if val < val_min:
        val_min = val

def trouver_val_neg (val: int) -> None:
    """

    :param val:
    :return:
    """





cpt = 1
nbr_val_neg = 0
while cpt <= 5:
    try:
        nbr = int(input("Veuillez entrer un nombre : "))
    except ValueError:
        print("veuiller entrer un nombre entier")
    else:
        if cpt == 1:
            val_min = nbr
        elif nbr < val_min:
            val_min = nbr
        if nbr < 0:
            nbr_val_neg = nbr_val_neg + 1
        cpt += 1

print("Le minimum des 5 valeurs est : ", val_min)
print("Le nombre de valeurs négatives est : ", nbr_val_neg)