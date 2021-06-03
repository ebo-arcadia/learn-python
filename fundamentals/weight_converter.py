weight = input("Enter your weight: ")
lbsOrKilos = input("(L)bs or (K)ilos? ")

# refactor
if lbsOrKilos.upper() == "L":
    converted = int(weight) * 0.45
    print(f"You are {converted} kilos")
else:
    converted = int(weight) // 0.45
    print(f"You are {converted} pounds")

# brute force solution
if lbsOrKilos == "L":
    result = int(weight) * 0.45
    print(f'Your are {result} pounds')
elif lbsOrKilos == "K":
    result = int(weight)
    print(f'Your are {result} kilos')
else:
    print("errors. enter again!")
    
