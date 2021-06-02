# example program
print("My name is Ebo")
print('o----')
print(' ||||')
print('*' * 10) 

# variable
# integer, floating, string, list,...
price = 10
print(price)
price = 20
print(price)
rating = 4.5
print(rating)
name = "Ebo"
print(name)
is_developer = False
print(is_developer)

# exercise
name = "John Smith"
age = 20
is_new_patient = True

# receive input from user
# full_name = input('what is your name? ')
# color = input('what is your favorite color? ')
# print('yoo yoo ' + full_name + ' your fav color is ' + color)

# given a birth year, write a program to run the age
#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2021 - int(birth_year)
#print(type(age))
#print(age)

# exercise 
#weight_lbs = input('what is your weight in lbs? ')
#weight_kg = int(weight_lbs) * 0.45
#print(weight_kg)

# strings
course = "python's course for beginners"
course_1 = 'the name is "java"'
email = ''' 
hey there,
this is my first email string in python!

regards
Ebo
'''
print(course)
print(course_1)
print(email)
print(course[0])
print(course_1[-2])
print(email[1:10])
print(email[10:])
print(course[:3])
copy = course[:]
print(copy)

# formatted string
# useful dynamcially tag something
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a good developer! '
formatted_msg = f'{first} {last} is an excellent developer '
print(message)
print(formatted_msg)

# string methods
# using len to limit input characters
string = 'this is a string and java is added'
print(len(string))
upper = string.upper()
print(upper)
print(string)
print(string.lower())
find = string.find('string')
print(find)
replace = string.replace('string', 'python character')
print(replace)
print('java' in string)

# arithmetic operations
print(10 + 3)
print(10 - 4)
print(10 * 3)
print(10 % 3)
print(10 // 3)
print(10 / 3)
print(10 ** 3)

x = 10
# x  = x + 3
x += 10
print(x)
x -= 1
print(x)

# operation procedures
y = 10 + 3 * 10 ** 2 / 10
print(y)
z = (10 + 3) * 10 ** 2 / 10 - 3
print(z)

# math function
f = 3.11232
print(round(f))
print(abs(-10.1))

import math
print(math.ceil(2.9))
print(math.floor(2.9))
# search python 3 module documentation

# if statement
is_hot = False
is_cold = True

if is_hot:
    print("It is real hot!")
    print("take care of your self!")
elif is_cold:
    print("it is not hot but cold!")
    print("go sleep")
else:
    print("neither cold nor hot!")
print("always here!")

# exercise
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price 
    # print(down_payment)
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# logical operations
has_high_income = True
has_good_score = False

# and: both
if has_good_score or has_high_income:
    print("eligble for loans!")
    
if has_good_score and has_high_income:
    print("eligble for loans!")

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("eligble for loan witout criminal record???")
    
# compare operations
temp = 35

if temp == 30:
    print("it is really hot!")
else:
    print("not hot at all")

# exercise
letter = "Leon"

if len(letter) < 3:
    print("name must be at least 3 characters!")
elif len(letter) > 10:
    print("name can not be more than 50 characters!")
else:
    print("it looks good!")
    
# while loops
index = 1
while index <= 10:
    print('*' * index)
    index = index + 1
    print("next loop...")
print("Done")

# for loops
for item in [5, 'string', 'sun', 'moon']:
    print(item)
    
for item in range(3, 20, 3):
    print(item)
    
# nested loop
for x in range(4):
    for y in range (5):
        for z in range (3):
            print(f"({x}, {y}, {z})")
            
#lists
name = ['john', 'matt', 'luke', 'mark']
print(name)
print(name[0])
print(name[-1])
print(name[2:3])
name[0] = 'james'
print(name)

numbers = [100, 123, 1, 10, 5, 45]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2-dimensinal list
matrix = [
    [1,2,3],
    [4,5,6],
    [6,7,8]
]
matrix[0][2] = 1000
print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)
        
numbers = [4,3,1,5,6,12, 4, 4]
numbers.append(13)
numbers.pop()
print(numbers)
numbers.insert(0, 100)
print(numbers)
numbers.remove(4)
print(numbers)
# numbers.clear()
print(numbers)
print(100 in numbers)
print(numbers.count(5))
print(numbers)
numbers.sort()
print(numbers)
number2 = numbers.copy()

# tuples
nums = (1,2,3)
#nums[0] = 1022
print(nums[0])

# unpacking 
coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates
print(x)

# dictionaries
customer = {
    "name": "john",
    "age": 33,
    "is_verified": True
}

customer["name"] = "new name"
print(customer["name"])
print(customer.get("name", "1988"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}

output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)

# 