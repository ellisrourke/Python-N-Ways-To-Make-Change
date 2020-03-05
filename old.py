def sumCombinations(sum,numbers):
    #Generate 0's array to represent possible combinations
    combinations = [[0 for collumns in range(sum+1)] for rows in range(len(numbers)+1)]
    #for i in range(len(numbers)+1):
    #   print(combinations[i])

    #initialise first space to 1 combinations[0][0]
    combinations[0][0] = 1

    #for i in range(len(numbers)+1):
        #print(combinations[i])

    for row in range(1,len(numbers)):
        print(len(numbers))
        for collumn in range(0,sum):
            #print(row,collumn)
            #print(combinations[row][collumn])
            if collumn == 0:
                combinations[row][collumn] = 1
            elif(row!=0):
                combinations[row][collumn] = combinations[row-1][collumn]
                if(numbers[row] <= collumn):
                    combinations[row][collumn] += combinations[row][collumn-numbers[row]]

    return(combinations[len(numbers)-1][sum])
    #for row in range(0, len(numbers) + 1):
    #    print(combinations[row])

# === MAIN FUNCTION == #
#define allowed values and value to be summed to
sum = 5
numbers = [0,1,2,3,5]
print(sumCombinations(sum,numbers))


