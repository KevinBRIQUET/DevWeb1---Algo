#Calculez le volume d’un parallélépipède dont la largeur, la longueur et la hauteur seront saisies au  clavier. 

print("---> Calcul du volume d'un parallélépipède <---")
largeur = float(input("Veuillez saisir la largeur du parallélépipède en cm (appuyez sur entrée pour valider): "))
longueur = float(input("Veuillez saisir la longueur du parallélépipède en cm (appuyez sur entrée pour valider): "))
hauteur = float(input("Veuillez saisir la hauteur du parallélépipède en cm (appuyez sur entrée pour valider): "))
volume = largeur * longueur * hauteur
print(f"le volume d'un parallélépipède est {volume} cm³")