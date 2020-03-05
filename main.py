def sumCombinations(sum,numbers):
    c = [0]*sum #min coins for p cents
    s = [0]*sum #last coin used, tracks optimal solution
    currentCoin = numbers[0]
    for p in range(1,sum):
        if(c[p] < currentCoin):
            c[p] = p
        elif(c[p+1] in numbers):
             = numbers[0]
            #currentCoin = numbers[currentCoin+1]
        print(c[p],end=" ")






# === MAIN FUNCTION == #
#define allowed values and value to be summed to
sum = 16
numbers = [1,5,12,25]
print(sumCombinations(sum,numbers))


