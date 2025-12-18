def part1 ():

    lines = []

    
    with open("input.txt") as file:
        lines = file.readlines()
    
    firstList = []
    secondList = []

    for i in range(len(lines)):
        firstList.append(int(lines[i].split(' ')[0]))
        secondList.append(int(lines[i].split(' ')[-1]))

    firstList.sort()
    secondList.sort()
    
    total = 0 

    for i in range(len(firstList)):
        total += abs(firstList[i] - secondList[i])
    
    print(total)

part1()

