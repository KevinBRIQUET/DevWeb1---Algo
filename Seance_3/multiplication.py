
#Affichez une table de multiplication (jusqu’à 10) dont l’ordre (le nombre concerné) sera saisi au  clavier. 
print("---> Affichez table de multiplication <---")
print()


table = int(input("Ecrire le nombre :"))
for table in range(0,11):
    print(table * table)

