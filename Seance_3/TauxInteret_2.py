# Jean a un livret A avec 2000 euros dessus au taux d’intérêt de 2%
# - Modifier le programme pour pouvoir choisir le taux d’intérêt et le nombre d’années

# ( 2 * 2000 / 100 ) = 40

print("="*100)

livret = int(input("Combien d'argent sur le livret A ? : "))
year = int(input("Combien d'années cet argent sera t'il de coté ? : "))
taux = int(input("Combien d'interêt par an en % ? : "))

for i in range(year) :
    interet = livret * taux /100
    livret = interet + livret
print(f"Au bout de {year} ans, vous aurez sur votre livret A : {round(livret,2)} €")

print("="*100)
