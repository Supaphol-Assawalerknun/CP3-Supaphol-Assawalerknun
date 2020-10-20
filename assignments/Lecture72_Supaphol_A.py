menuList = []

def totalprice():
    sum = 0
    for price in range(len(menuList)):
        price = int(menuList[price][1])
        sum = sum+price
    print("your total price is %d THB Thank you!" % (sum))

def showBill():
    print("Total Bill".center(30, "-"))
    for food in range(len(menuList)):
        print(menuList[food][0], menuList[food][1], " THB")
    return totalprice()


while True:
    menuName = input("Please enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append([menuName, menuPrice])

showBill()
