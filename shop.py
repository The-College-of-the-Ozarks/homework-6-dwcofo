# shop.py
#
# 
# fcts
import re


# DWTODO read the files
# create a file

def printLists(book, tBook):
    print(f"The items the shop is willing to {tBook}.")
    for x in book:
        print(f'{x:20}  ${book[x]}')


def priceCheck(prompt):
    # https://docs.python.org/3/library/re.html
    pattern = re.compile('^[0-9]*\.[0-9]{2}$')
    price = input(f"{prompt} (Form .00): ")
    while not pattern.match(price) and float(price) <= 0:
        price = input(f"Error: invalid price. {prompt} (Form .00): ")
    return price


def newItem(book, tBook):
    item = input(f"What item do you want to {tBook}: ")
    words = "provide" if tBook == "sell" else "want"
    if item in book:
        print(f"I'm sorry, but we already {words} {item} at ${book[item]}")
        return

    book[item] = priceCheck("What will be the price of {item} in dollars")


def alterItem(book, tBook):
    item = input("What item do you want to change the price for: ")
    words = "provide" if tBook == "sell" else "want"
    if item not in book:
        print(f"I'm sorry, but we don't {words} {item}")
        return

    book[item] = priceCheck("What is the new price of {item} in dollars")


buy = {}
sell = {}
shopMoney = 0

# I got this from https://docs.python.org/3/tutorial/inputoutput.html
lines = []
with open('bad_list.dat') as f:
    lines = f.readlines()

# print(lines)
for i, x in enumerate(lines):
    temp = x.split("\t")
    # print(temp[2].strip())
    if len(temp) != 3:
        print(f"Error on line {i + 1}: Not the correct amount of segments")
        continue
    if temp[0] != "Buy" and temp[0] != "Sell":
        print(f"Error on line {i + 1}: Not a Buy or Sell order")
        continue
    if (temp[0] == "Buy" and temp[1] in buy) or (temp[0] == "Sell" and temp[1] in sell):
        print(f"Error on line {i + 1}: Already in the books")
        continue
    if not re.search('^\$[0-9]+\.*[0-9]*$', temp[2].strip()):
        print(f"Error on line {i + 1}: Improper price format")
        continue
    if temp[0] == "Buy":
        buy[temp[1]] = float(temp[2][1:])
    elif temp[0] == "Sell":
        sell[temp[1]] = float(temp[2][1:])

while True:

    print(f'Current shop money: ${shopMoney:<10.2f}')
    userIn = input(
        "1) Print buy list\n2) Print sell list\n3) Buy item\n4) Sell item\n5) Add item\n6) Change price of an item\n7) Quit\nYour choice: ")
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
            print(f"We don't want {item}.")
    elif userIn == "4":
        # Sell item
        item = input("What item would you like to Sell? ")
        if item in sell:
            shopMoney += sell[item]
            sell.pop(item)
        else:
            print(f"{item} is not for sale.")
    elif userIn == "5":
        # Add item to Buy or Sell list
        while True:
            option = input("So, You have an idea for the shop?\n1) Buy\n2) Sell\n3) Cancel\nWhich is it: ")
            if option == "1":
                newItem(buy, "buy")
                break
            elif option == "2":
                newItem(sell, "sell")
                break
            elif option == "3":
                break
    elif userIn == "6":
        # Change price of item in Buy or Sell list
        while True:
            option = input("Which price do you want to alter?\n1) Buy\n2) Sell\n3) Cancel\n: ")
            if option == "1":
                alterItem(buy, "buy")
                break
            elif option == "2":
                alterItem(sell, "sell")
                break
            elif option == "3":
                break
    elif userIn == "7" or userIn.lower() == "quit":
        # Quit
        break
    else:
        print("Please input a valid option.")

outputFile = input(
    "What file do you want the sale data to be stored in? (Format: only letters and numbers separated with _ don't include the extension): ")
while not re.search('^\w+$', outputFile):
    outputFile = input(
        "What file do you want the sale data to be stored in? (Format: only letters and numbers separated with _ don't include the extension): ")


fileData = [f"Buy\t{x}\t${buy[x]}\n" for x in buy]
fileData.extend([f"Sell\t{x}\t${sell[x]}\n" for x in sell])
# I got this from https://docs.python.org/3/tutorial/inputoutput.html
locFile = open(f"{outputFile}.dat", "w")
locFile.writelines(fileData)
locFile.close()
print(f"Money from this session is {shopMoney}\nGoodbye!")
