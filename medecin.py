numeroPermis = []
for annee in range(1930, 2018):
    anneeCourt = str(annee % 100).zfill(2)
    for index in range(0, 1000):
        indexFill = str(index).zfill(3)
        numeroPermis.append(anneeCourt + indexFill)
print(numeroPermis)
