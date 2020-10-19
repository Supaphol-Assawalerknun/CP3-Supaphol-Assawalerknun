'''อย่ามองโปรแกรมเป็นปัญหาใหญ่อันเดียว ให้แยกเป็นปัญหาย่อยๆหลายปัญหา'''
def loginSection() :
    usernameInput = input("insert username: ")
    passwordInput = input("insert password: ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu() :
    print("----------------SA shop-----------------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect() :
    item = int(input("Please select item: "))
    if item == 1:
        return vatCalculate(int(input("Please insert price: ")))
    elif item == 2:
        return priceCalculate()
    else:
        print("Wrong option, Please try again")
        return menuSelect()

def vatCalculate(totalprice) :
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result

def priceCalculate() :
    price1 = int(input("first product price: "))
    price2 = int(input("second product price: "))
    return vatCalculate(price1 + price2)

while loginSection() == False :
    print("Wrong username or password, Please try again")

print(showMenu())
