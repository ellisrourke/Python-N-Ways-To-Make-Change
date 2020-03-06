import time
class coinRecursion():
    def sieve(self):
        print("Calculating Sieve of Eratosthenes")
        return [1,2,3,5,6,7,8,9]

    def __init__(self):
        amount = 5
        coins = self.sieve()
        print(self.coinChange(amount,coins,0),"solutions found in",time.process_time(),"seconds")

    def coinChange(self,amount,coins,currentCoin):
        print(self.count,currentCoin,amount)

        if(amount == 0):
            return 1
        if(amount < 0):
            return 0

        combinations = 0

        for i in range(currentCoin,len(coins)):
            combinations += self.coinChange(amount - coins[i],coins,i)

        return combinations

solve = coinRecursion()
#print(solve," solutions found - Time taken (secs) = ", time.process_time())

