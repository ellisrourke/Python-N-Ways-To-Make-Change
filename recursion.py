
class coinRecursion():
    coins = [1, 2]
    amount = 4

    def __init__(self):
        print(self.coinChange(self.amount,self.coins))


    def coinChange(self,amount,coins):
        if(amount == 0):
            return 1
        if(amount < 0):
            return 0

        combinations = 0

        #for coin in self.coins:
        for i in range(0,len(self.coins)):
            combinations += self.coinChange(amount - coins[i],coins)

        return combinations

solve = coinRecursion()
