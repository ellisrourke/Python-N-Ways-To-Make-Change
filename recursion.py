
def coinChange(coins, remainder, cache):
    if(remainder < 0):
        return -1

    if(remainder == 0):
        return 0

    if(cache[remainder]!=0):
        return cache[remainder]

    min = 0
    for coin in coins:
        change = coinChange(coins,remainder-coin,cache)

        if(change >= 0 and change < min):
            min = 1 + change

        #???
        min = -1

        return cache[remainder]


coins = [1,2,3]
amount = 5
cache = [0]*(amount+1)
coinChange(coins,amount,cache)