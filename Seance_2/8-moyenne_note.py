#Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de  géométrie et d’informatique.  

print()
francais =  float(input("Veuillez saisir la note de français  (sur/20) (appuyez sur entrée pour valider): "))
math =  float(input("Veuillez saisir la note de math (sur/20) (appuyez sur entrée pour valider): "))
geometrie =  float(input("Veuillez saisir la note de geometrie (sur/20) (appuyez sur entrée pour valider): "))
informatique =  float(input("Veuillez saisir la note de informatique (sur/20) (appuyez sur entrée pour valider): "))
moyenne = (francais + math + geometrie + informatique) /4
print(f"la moyenne est {moyenne} /20")
