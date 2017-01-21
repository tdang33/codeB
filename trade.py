from api import networth, my_securities, getdata, setOrder, getOrders
import threading

stocks = ['' for i in range(0,10)]

value = []

cur_orders = [[] for i in range(0, 10)]

myshares = [[0,0]]*10

data = [[] for i in range(0,10)]

# update the networth of my portfolio. Initially, it is $5000.
def updateNetworth():
  current_net = networth()
  value.append(current_net)
  # print value

# update the number of shares of each stock in my portfolio
def updateMySecurities():
    securities = my_securities()
    for i in range(0, 10):
        stocks[i] = securities[3*i + 1]
        myshares[i][0] = float(securities[3*i + 2])
        myshares[i][1] = float(securities[3*i + 3])
    # print stocks

# get networth, dividend, volatility at each second of every stock
def updateData():
    newData = getdata()
    for i in range(0, 10):
        value = float(newData[4*i + 2])
        div = float(newData[4*i + 3])
        var = float(newData[4*i + 4])
        data[i].append([value, div, var])
    # print data[0]

def updateOrders():
    for k in range(0, 10):
        ticker = stocks[k]
        orders = getOrders(ticker)
        length = len(orders)
        i = 1
        new_orders = [[] for i in range(0, 2)]
        while (i < length):
            trade = orders[i]
            price = float(orders[i + 2])
            vol = float(orders[i + 3])
            if (trade == 'BID'):
                new_orders[0].append([price, vol])
            else:
                new_orders[1].append([price, vol])
            i = i + 4
        cur_orders[k] =  new_orders
    print cur_orders
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
update()

# trade()
