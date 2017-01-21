from client2 import run
print "abcd"

user = 'vnexpress'
password = 'vietnamno1'

def networth():
    return float(run(user, password, 'MY_CASH').split()[1])

# print networth()

def my_securities():
    return run(user, password, 'MY_SECURITIES').split()

def getdata():
    return run("vnexpress", "vietnamno1", 'SECURITIES').split()

def setOrder(command):
    run("vnexpress", "vietnamno1", command)
# print run("vnexpress", "vietnamno1", 'MY_CASH')
#
# print run("vnexpress", "vietnamno1", 'MY_SECURITIES')
#
# print
#
# print run("vnexpress", "vietnamno1", 'MY_ORDERS')
#
# print
#
# run("vnexpress", "vietnamno1", 'ORDERS AMZN')
#
# print

# print run("vnexpress", "vietnamno1", 'SECURITIES')

# run("vnexpress", "vietnamno1", 'SECURITIES')

#
# print run("vnexpress", "vietnamno1", 'BID DIS 20.1 40')
# BID <ticker> <price> <shares>
