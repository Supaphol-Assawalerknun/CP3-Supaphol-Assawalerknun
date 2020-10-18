def vatCalculate (totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price= int(input("Price : "))
print(vatCalculate(price))