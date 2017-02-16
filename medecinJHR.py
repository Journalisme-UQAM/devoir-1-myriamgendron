numeroPermis = []
for annee in range(1930, 2018):
    anneeCourt = str(annee % 100).zfill(2) # Cool! Je ne connaissais pas la méthode zfill :)
    for index in range(0, 1000):
        indexFill = str(index).zfill(3)
        numeroPermis.append(anneeCourt + indexFill)
# print(numeroPermis)

# Ça marche très bien!
# Pour afficher chaque numéro de permis sur une ligne, il aurait suffi de faire une boucle dans la liste que tu as créée.

for num in numeroPermis:
	print(num)