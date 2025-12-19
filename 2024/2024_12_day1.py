def part1 ():

    lines = []

    # Permet de récuperer les données dans input.txt lignes par lignes
    with open("input.txt") as file:
        lines = file.readlines()
    
    # Création de 2 listes 
    firstList = []
    secondList = []

    # Parcours le tableau récuperé depuis input.txt
    for i in range(len(lines)):
        #Ajoute dans le tableau firstList l'entier de la 1ère valeur de la ligne
        firstList.append(int(lines[i].split(' ')[0]))
        #Ajoute dans le tableau secondList l'entier de la dernière valeur de la ligne
        secondList.append(int(lines[i].split(' ')[-1]))

    # Tri des 2 listes
    firstList.sort()
    secondList.sort()
    
    total = 0 

    # Parcours mes listes pour calculer la différence et l'ajouter au total
    for i in range(len(firstList)):
        total += abs(firstList[i] - secondList[i])
    
    # Affiche le total
    print(total)



def part2 ():
    lines = []

    # Permet de récuperer les données dans input.txt lignes par lignes
    with open("input.txt") as file:
        lines = file.readlines()
    
    # Création de 2 listes 
    firstList = []
    secondList = []

    # Parcours le tableau récuperé depuis input.txt
    for i in range(len(lines)):
        #Ajoute dans le tableau firstList l'entier de la 1ère valeur de la ligne
        firstList.append(int(lines[i].split(' ')[0]))
        #Ajoute dans le tableau secondList l'entier de la dernière valeur de la ligne
        secondList.append(int(lines[i].split(' ')[-1])) 
    
    similar = 0

    for i in range(len(firstList)):  
        nbOccurence = 0
        for j in range(len(secondList)):
            if (firstList[i] == secondList[j]):
                nbOccurence += 1
        similar += firstList[i]*nbOccurence

    print(similar)

part1()
part2()