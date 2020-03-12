def change(n, coins_available, coins_so_far,upperLim):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	elif(len(coins_so_far) >= upperLim):
		pass
	else:
		for c in change(n, coins_available, coins_so_far+[coins_available[0]],upperLim):
			yield c
		for c in change(n, coins_available[1:], coins_so_far,upperLim):
			yield c

if __name__ == '__main__':
	n = 15
	lim = 15
	coins = [1,2,3,5,7]


	solutions = change(n, coins, [],lim)
	for s in solutions:
		print(s)

