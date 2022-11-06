print("This is a Simple CLI Calculator")
print("1/Factorial calculator\n2/Area of Circle: ")

while True:
    a = int(input("\nSellect: "))
    if a == 1:
        import check
    elif a == 2:
        import Star
    elif a == "q":
        break
    else:
        pass