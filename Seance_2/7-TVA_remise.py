#Saisissez le prix unitaire HT d’un produit et la quantité commandée. 
# Calculez le montant HT de la  commande,appliquez une remise de 15% et 
# calculez le prix TTC après avoir saisi le taux de TVA.  



# def prixUnit(prixUnit : int, qte : int, tva : float):
#     HTetTTC = []
#     remise : float = 0.85
#     res = 0

#     res = prixUnit * qte
#     res += res * tva
#     HTetTTC.append(res)
#     res *= res*tva
#     HTetTTC.append(res)

#     return HTetTTC

# print(prixUnit(50, 10, 1.20))


def addition(a, b):
    return a + b

print(addition(5, 6))

a = 5
b = 6

print(a+b)






















# print("---> Calcul remise <---")
# print()
# HT = float(input("Saisir le prix unitaire HT :"))
# quantite = int(input("Saisir la quantité commandée :"))
# montantHT = (HT * quantite) * 0.85
# TVA = float(input("Saisir le taux de TVA en % :"))
# montant_avec_TVA = montantHT + montantHT * (TVA/100)
# print(f"Le montant hors taxe est de {montantHT} le prix de l'article avec la TTC et la TVA est de {montant_avec_TVA} €") 