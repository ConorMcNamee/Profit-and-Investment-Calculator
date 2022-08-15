#!usr/bin/python

import sys, getopt
import os

def expo_returns(days, percent_profit, investment_amount):

    new_investment_amount = 0

    if(int(days) > 0):
        investment_increase = ( float(investment_amount) / 100 ) * float(percent_profit)
        new_investment_amount = float(investment_amount) + investment_increase
        print(round(new_investment_amount, 2), " Investment Increase: ", round(investment_increase, 2))
        expo_returns(int(days) - 1, percent_profit, new_investment_amount)

def profit(buy_price, sell_price):
    profit = int(sell_price) - int(buy_price)
    return profit

def main(argv):

    buy_price = 0
    sell_price = 0

    days = 0
    percent_profit = 0
    investment_amount = 0

    try:
        opts, args = getopt.getopt(argv, "hp:e")
    except getopt.GetoptError:
        print("usage: main.py -p <buy price> <sell price> \n ")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -p <buy price> <sell price> \n -e: <days>, <percent_profit>, <investment_amount>')
            sys.exit()
        elif opt in ("-p", "--profit"):
            print(profit(argv[1], argv[2]))
        elif opt in ("-e", "--expo"):
            expo_returns(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    main(sys.argv[1:])
