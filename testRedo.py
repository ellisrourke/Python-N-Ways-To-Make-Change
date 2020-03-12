import time

#todo research generator
#optimal memory space
def calculateChange(n, availableCoins, usedCoins,lowerLimit,upperLimit):
    # if sum of coins is answer, return combination

    if (len(usedCoins) > upperLimit):
        pass
    elif (sum(usedCoins) == n and len(usedCoins) in range(lowerLimit,upperLimit+1)):
        yield usedCoins
    elif (sum(usedCoins) > n):
        pass
    elif availableCoins == []:
        pass


    else:
        for i in calculateChange(n, availableCoins, usedCoins + [availableCoins[0]],lowerLimit,upperLimit):
            print(usedCoins, [availableCoins[0]])

            yield i
        for i in calculateChange(n,availableCoins[1:],usedCoins,lowerLimit,upperLimit):
            yield i


n = 5
lowerLimit = 1
upperLimit = 10
coins = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,87]
'''
101,103,107,109,113,127,131,   137,    139,    149,    151,    157,    163,    167,    173,
    179,    181,    191,    193,    197,    199,    211,    223,    227,   229,
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281,
    283,    293,    307]
'''
combinations = list(calculateChange(n,coins,[],lowerLimit,upperLimit))

#for solution in combinations:
    #print(solution)
print(sum(1 for i in combinations),"Solutions found")
print("Time taken (secs) = ", time.process_time())