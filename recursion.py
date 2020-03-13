import time
validSolutions = 0

def coins():
    return [1,2,3,5,6,7]

def coinChange(amount,coins,currentCoin,recursiveDepth):
    current = []
    if(amount == 0):
        current.append(coins[currentCoin])
        return 1
    if(amount < 0):
        return 0
    combinations = 0
    for i in range(currentCoin,len(coins)):

        current.append(currentCoin)
        combinations += coinChange(amount - coins[i], coins, i, recursiveDepth - 1)
    print(current)
    return combinations


amount = 5
recusiveDepth = 5
goal_state = recusiveDepth
coins = coins()
print(coinChange(amount, coins, 0, recusiveDepth), "solutions found in", time.process_time(), "seconds")

