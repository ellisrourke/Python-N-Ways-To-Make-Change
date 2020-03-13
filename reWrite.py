import time

def calculateChange(n, availableCoins, usedCoins,lowerLimit,upperLimit,solutions):
    if(sum(usedCoins) == n and len(usedCoins) in range(lowerLimit,upperLimit+1)):
        if(usedCoins not in solutions):
            solutions += [usedCoins]
        return usedCoins
    elif(len(usedCoins) > upperLimit):
        return 0

    elif(sum(usedCoins) > n):
        return 0

    elif(availableCoins == []):
        return 0

    else:
        calculateChange(n, availableCoins[1:], usedCoins, lowerLimit, upperLimit,solutions)
        calculateChange(n, availableCoins, usedCoins + [availableCoins[0]], lowerLimit, upperLimit,solutions)
n = 100
lowerLimit = 8
upperLimit = 25
coins = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,87]


solutions = []
calculateChange(n,coins,[],lowerLimit,upperLimit,solutions)
for solution in solutions:
    print(solution)
print(len(solutions),"solutions found in", time.process_time(),"seconds")