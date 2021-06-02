try:
    age = int(input('Age: '))
    income = 6000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can not be zero...")
except ValueError: 
    print("Invaid value...")
    
