from api import networth, my_securities, getdata, setOrder

import threading

stocks = ['' for i in range(0,10)]

value=[]
myshares = [[0,0]]*10
data = [[] for i in range(0,10)]


def updateNetworth():
  current_net = networth()
  value.append(current_net)
  # print value

def updateMySecurities():
    securities = my_securities()
    for i in range(0, 10):
        stocks[i] = securities[3*i + 1]
        myshares[i][0] = float(securities[3*i + 2])
        myshares[i][1] = float(securities[3*i + 3])
    print stocks

def updateData():
    newData = getdata()
    for i in range(0, 10):
        price = float(newData[4*i + 2])
        div = float(newData[4*i + 3])
        var = float(newData[4*i + 4])
        data[i].append([price, div, var])
    # print data[0]



def bid(index, price, share):
    setOrder('BID ' + str(stocks[index]) + ' ' + str(price) + ' ' + str(share))

def ask(index, price, share):
    setOrder('ASK ' + str(stocks[index]) + ' ' + str(price) + ' ' + str(share))




def update():
  threading.Timer(1.0, update).start()
  updateNetworth()
  updateMySecurities()
  updateData()
  print

# print getdata()
bid(0, 100.5, 10.5)
update()

# trade()
