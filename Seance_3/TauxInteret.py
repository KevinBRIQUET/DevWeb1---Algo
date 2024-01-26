# Jean a un livret A avec 2000 euros dessus au taux d’intérêt de 2%
# - Ecrire un programme pour savoir combien il aura dans 10 ans

# ( 2 * 2000 / 100 ) = 40
print("="*100)


livret = 2000


for i in range(10) :
    interet = livret * 2 /100
    livret = interet + livret
print(f"Au bout de 10 ans, vous aurez sur votre livret A : {round(livret,2)} €")







print("="*100)
