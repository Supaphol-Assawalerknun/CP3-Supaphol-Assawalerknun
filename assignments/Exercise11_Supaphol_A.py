number = int(input("How many floors of pyramid do you want?: "))
for x in range(number):
    print((" "*number)+"*"*x+("*"*(x+1))+(" "*number))
    number -= 1

