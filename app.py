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