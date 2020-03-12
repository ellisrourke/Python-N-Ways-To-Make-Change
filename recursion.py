import time
class coinRecursion():
    def coins(self):
        return [1,2,3,5,6,7,9]

    def __init__(self):
        amount = 8
        coins = self.coins()
        recusiveDepth = 3
        goal_state = recusiveDepth
        print(self.coinChange(amount,coins,0,recusiveDepth),"solutions found in",time.process_time(),"seconds")

    def coinChange(self,amount,coins,currentCoin,recursiveDepth):
        if(recursiveDepth <= 0):
            return 0
        if(amount == 0):
            print("recursive depth",recursiveDepth," amount",amount)
            return 1
        if(amount < 0):
            return 0

        combinations = 0

        for i in range(currentCoin,len(coins)):
         combinations += self.coinChange(amount - coins[i], coins, i, recursiveDepth - 1)

        return combinations

solve = coinRecursion()

