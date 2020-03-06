
class coinRecursion():
    coins = [1, 2]
    amount = 4
    currentCoin = coins[0]
    def __init__(self):
        print(self.coinChange(self.amount,self.coins,self.currentCoin))


    def coinChange(self,amount,coins,currentCoin):
        print(currentCoin)
        if(amount == 0):
            return 1
        if(amount < 0):
            return 0

        combinations = 0

        #for coin in self.coins:
        for i in range(currentCoin,len(self.coins)):
            combinations += self.coinChange(amount - coins[i],coins,i)


        return combinations

solve = coinRecursion()
