usernameInput = input("insert username: ")
passwordInput = input("insert password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("log in success!!")
    print("----------------SA shop-----------------")
    print("what do you want today?")
    print("1. Pens (50pcs./box)      :  50  THB")
    print("2. Photocopy papers (box) : 200  THB")
    print("3. Paper clips (box)      :  25  THB")
    print("Note: all item not included VAT")
    item = int(input("Please select item: "))
    if item == 1:
        product = int(input("How many do you want? (box): "))
        price = 50
        vat = 7
        result = (price + (price * vat / 100))*product
        print("Total (VAT included) = ", result, "THB")
        print("----------Thank you-----------")
    elif item == 2:
        product = int(input("How many do you want? (box): "))
        price = 200
        vat = 7
        result = (price + (price * vat / 100)) * product
        print("Total (VAT included) = ", result, "THB")
        print("----------Thank you-----------")
    elif item == 3:
        product = int(input("How many do you want? (box): "))
        price = 25
        vat = 7
        result = (price + (price * vat / 100)) * product
        print("Total (VAT included) = ", result, "THB")
        print("----------Thank you-----------")
    else:
        print("ERROR please choose again...")
else:
    print("incorrect please input again")