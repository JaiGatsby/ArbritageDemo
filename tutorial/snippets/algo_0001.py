from snippets.toHeroku import postIt, getStock

QTY = "10"

def algo(n):
	# Something
	# print("occurrance number ",n)
	if n == 0:
		return
	ask, bid,askurl,bidurl = getStock()
	return
	if ask <100 and ask>140:
		print("asking weirdly ",ask)
		return
	initial_price = ask
	postIt(askurl,"0001","buy",QTY,"limit",ask)
	print("Bought at ", ask)
	
	while True:
		ask, bid = getStock()
		print("Offered ",bid)
		if bid > initial_price:
			postIt(bidurl,"0001","sell",QTY,"limit",bid)
			break

	print("Sold")
	algo(n-1)
