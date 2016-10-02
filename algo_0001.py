from snippets.toHeroku import postIt, getStock

QTY = "10"

def algo(n):
	# Something
	# print("occurrance number ",n)
	arr = ["0001","0005","0386","0388","3988"]
	curIter = n%5
	print("in algo", arr[curIter])
	if n == 0:
		return
	ask, bid,askurl,bidurl = getStock(arr[curIter])
	if ask < 1 and ask > 300:
		return
	initial_price = ask
	postIt(askurl,arr[curIter],"buy",QTY,"market")
	print("Bought at ", ask)
	nmn = 30
	#fuckEmUp(2,"0001")
	profitC = 0
	while True:
		ask, bid, askurl,bidurl = getStock(arr[curIter])
		profit = bid - initial_price
		print("Profit ",profit)

		if profit>0:
			profitC = profitC+1

		if profitC > 4:
			postIt(bidurl,arr[curIter],"sell",QTY,"market")

		if nmn ==0:
			postIt(bidurl,arr[curIter],"sell",QTY,"market")
			break
		if bid - initial_price > 0.1:
			postIt(bidurl,arr[curIter],"sell",QTY,"market")
			break

		nmn = nmn-1

	print("Sold")
	algo(n-1)
