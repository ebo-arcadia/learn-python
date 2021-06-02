# function
# parameters

def greet_user(name, age):
    print(f"what's up {name}? your age: {age}")
    print("learning python is fine!")

# keyword args
print("Start")
greet_user(age=13, name="James")
greet_user(name="Neo", age=23)
print("done")

def square(number):
    return number * number


print(square(3))

