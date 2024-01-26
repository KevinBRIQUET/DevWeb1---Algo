# Palindrome : faire un programme ou l'utilisateur saisi un mot et le programme lui dit si c'est un palindrome ou non.

# - pas de liste
# - pas de notation [::-1]
# - pas de string.reverse
print("="*100)

mot = str(input("Veuillez écrire un mot : "))
if len(mot) %2 == 1:
	longueur = int((len(mot)-1)/2)
else :
	longueur = int(len(mot)/2)
for lettre in range (0,longueur):
	if mot[lettre] != mot[(len(mot)-1)-lettre]:
		réponse = "non"
		break
	else :
		réponse ="oui"
if réponse =="non" :
	print("Le mot n'est pas un palindrome")
else :
	print("Le mot est un palindrome")

print("="*100)