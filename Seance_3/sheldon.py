# THE FRIENDSHIP ALGORITHM
from time import sleep
print("="*100)

oui = ("oui")
non = ("non")

print("----> TUTO : SE FAIRE DES AMIS <----")
print ("Vous appelez votre (futur) pote : ")
print("Le téléphone sonne . . .")
print("Es tu à la maison ?")
print()
reponse = input("Répondre oui ou non : ")

if reponse == oui :
    print()
    print("On va manger un truc ?")
    reponse = input("Répondre oui ou non : ")
    if reponse == oui :
        print()
        print("Vous mangez ensemble ...")
        print() 
        print("Félicitations, vous êtes amis !")
    else :
        reponse == non 
        print("On va boire une boisson chaude ?")
        reponse = input("Répondre oui ou non : ")
        if reponse == oui :
            print()
            input("Tu veux quoi ? Thé ? Café ? Cacao ?")
            print()
            print("Félicitations, vous êtes amis !")
        else :
            print("On fait une activité ensemble ? Tu aime quoi ?")
            print("Il dit une activité ...")
            input("Tu es intéressé ? : ")
            n = 0
            if reponse == oui :
                print("Cool, faisont ça !")
                print("Félicitations, vous êtes amis !")
            else :
                n + 1
                print("Tu a une autre activité ?")
            
                    

else : 
    print("Laissez un message")
    print("Attendre qu'il rappelle")



