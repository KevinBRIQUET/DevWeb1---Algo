print("="*100)

mot = input("Saisir un mot : ")
tom =""
for lettre in mot:
    tom = lettre + tom
if mot == tom:
    print(f"Le mot {mot} est un palindrome")
else :
    print(f"Le mot {mot} n'est pas un palindrome")
        
print("="*100)