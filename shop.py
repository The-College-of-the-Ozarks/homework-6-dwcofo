# shop.py
#
# 
#fcts

def printLists(dict, type):
    print(f"The items the shop is willing to {type}.")
    for x in dict:
        print(f'{x:20}  ${dict[x]}')

    



buy = {
    "Watch 2":	50,
  	"Watch 3":	10
}
sell = {
    "Watch 4":	150,
	"Rolex":	99.99
}
shopMoney = 0





while True:
    
    print(f'Current shop money: ${shopMoney:<10.2f}')
    userIn = input("1) Print buy list\n2) Print sell list\n3) Buy item\n4) Sell item\n5) Add item\n6) Change price of an item\n7) Quit\nYour choice: ")
    if userIn == "1":
    # Print Buy list
        printLists(buy, "buy")
    elif userIn == "2":
    # Print Sell list
        printLists(sell, "sell")
    elif userIn == "3":
    # Buy item
        item = input("What item would you like to buy? ")
        if item in buy:
            shopMoney -= buy[item]
            buy.pop(item)
        else:
            print("That item is not for sale.")
    elif userIn == "4":
    # Sell item
        item = input("What item would you like to Sell? ")
        if item in sell:
            shopMoney += sell[item]
            sell.pop(item)
        else:
            print("That item is not for sale.")
    
    # Add item to Buy or Sell list
    # Change price of item in Buy or Sell list
    elif userIn == "7" or userIn.lower() == "quit":
    # Quit
        print("Goodbye!")
        break
    else:
        print("Please input a valid option.")