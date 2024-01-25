#Écrire un algorithme qui calcul le prix TTC à partir d’un prix HT et d’une TVA de 20 % (prestation  de service en France). 

print("---> Calcul de la TVA <---")
print()
HT = float(input("Ecrivez le prix Hors Taxe :"))
TVA = 20
TTC = HT + HT * TVA/100
print(f"le prix TTC est de {TTC} €")



# PSEUDO CODE

# TVA ← 20
# HT ← saisir
# TTC ← HT + HT * TVA/100
# afficher("Le prix TTC est"TTC, €)

