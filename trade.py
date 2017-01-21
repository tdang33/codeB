from api import networth, my_securities, getdata, setOrder, getOrders
import threading

stocks = ['' for i in range(0,10)]

value = []

cur_orders = [[] for i in range(0, 10)]

# prices[]

myshares = [[0,0]]*10

data = [[] for i in range(0,10)]

dividends = []

# update the networth of my portfolio. Initially, it is $5000.
def updateNetworth():
  current_net = float(networth())
  value.append(current_net)
  # print value

def getStocks():
    securities = my_securities()
    if (len(securities) < 30):
        return
    for i in range(0, 10):
        stocks[i] = securities[3*i + 1]

# update the number of shares of each stock in my portfolio
def updateMySecurities():
    securities = my_securities()
    if (len(securities) < 30):
        return
    for i in range(0, 10):
        # stocks[i] = securities[3*i + 1]
        myshares[i][0] = float(securities[3*i + 2])
        myshares[i][1] = float(securities[3*i + 3])
    # print myshares

# get networth, dividend, volatility at each second of every stock
def updateData():
    newData = getdata()
    if (len(newData) < 30):
        return
    for i in range(0, 10):
        # print newData[4*i + 2]
        value = float(newData[4*i + 2])
        div = float(newData[4*i + 3])
        var = float(newData[4*i + 4])
        data[i].append([value, div, var])
    # print data[0]

def updateOrders():
    # print stocks
    for k in range(0, 10):
        # print k
        ticker = stocks[k]
        # print ticker
        # print ticker
        orders = getOrders(ticker)
        length = len(orders)
        i = 1
        new_orders = [[] for i in range(0, 2)]
        while (i < length):
            trade = orders[i]
            stock = orders[i+1]
            # print trade
            if (stock not in stocks):
                return
            price = float(orders[i + 2])
            vol = float(orders[i + 3])
            if (trade == 'BID'):
                new_orders[0].append([price, vol])
            else:
                new_orders[1].append([price, vol])
            i = i + 4
        cur_orders[k] =  new_orders
        # print new_orders
    print cur_orders[0]
    print
    print



# send bid order. Index is the index of the stock, not the ticker
def bid(index, price, share):
    setOrder('BID ' + str(stocks[index]) + ' ' + str(price) + ' ' + str(share))

#send ask order
def ask(index, price, share):
    setOrder('ASK ' + str(stocks[index]) + ' ' + str(price) + ' ' + str(share))











# update the market data after each t seconds
def update():
    threading.Timer(1.0, update).start()
    updateNetworth()
    updateMySecurities()
    updateData()
    updateOrders()
    # print getOrders(stocks[0])
    print



# print getdata()
# bid(0, 100.5, 10.5)
getStocks()
update()

# trade()
