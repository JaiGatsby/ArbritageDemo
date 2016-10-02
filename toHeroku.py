import requests
import json
URL1 = ['http://cis2016-exchange1.herokuapp.com/api/market_data/','http://cis2016-exchange2.herokuapp.com/api/market_data/','http://cis2016-exchange3.herokuapp.com/api/market_data/']
URL2 = ['http://cis2016-exchange1.herokuapp.com/api/orders','http://cis2016-exchange2.herokuapp.com/api/orders','http://cis2016-exchange3.herokuapp.com/api/orders']

uid = "phOXgkF7ErYI2MYABLmc6A"
def postIt(exchange,symbol,side,qty,typey,price = -1):
	if price < 0:
		r = requests.post(URL2[exchange],data={"team_uid":uid,
		   "symbol" : symbol,
		   "side":side,
		   "qty":qty,
		   "order_type":typey})
	else:
		r = requests.post(URL2[exchange],data={"team_uid":uid,
		   "symbol" : symbol,
		   "side":side,
		   "qty":qty,
		   "order_type":typey,
		   "price":price})


def tofloat(arr):
    for i in range(len(arr)):
        arr[i] = float(arr[i])
    return arr

def fuckEmUp(rl,stock):
	a = requests.post(URL2[rl],data = {"team_uid":uid,
		   "symbol" : stock,
		   "side":"buy",
		   "qty":1,
		   "order_type":"limit",
		   "price": 1.0})
	todel = json.loads(a.text)
	delid = todel["id"]

	lol = requests.delete(URL2[rl]+'/'+delid)
	print(lol)

def unPack(res):
	res = json.loads(res.text)
	ask = list(res["sell"].keys())
	bid = list(res["buy"].keys())

	#print("ask ", ask, " - bid ", bid)
	ask = tofloat(ask)
	bid = tofloat(bid)
	ask = min(ask) if len(ask)>0 else 99999
	bid = max(bid) if len(bid)>0 else 0.0

	return ask,bid

def getStock(symb):
	print("stock", URL1[0]+symb)
	try:
		a = requests.get(URL1[0]+symb,timeout = 4)
		print(a)
		b = requests.get(URL1[1]+symb, timeout=4)
		print(b)
		c = requests.get(URL1[2]+symb,timeout=4)
		print(c)
	except:
		getStock(symb)
	a1,b1 = unPack(a)
	a2,b2 = unPack(b)
	a3,b3 = unPack(c)

	ask = min(a1,a2,a3)
	bid = max(a1,b2,b3)

	askurl = 0 if a1==ask else (1 if a2 ==ask else 2)
	bidurl = 0 if b1==bid else (1 if a2 ==ask else 2)

	#print("Ask: ",ask,"Bid:",bid,"askurl:",askurl,"bidurl:",bidurl)
	return ask,bid, askurl, bidurl