numbers = [2,2,2,4,5,6,7,7,8,20,23,23,45,34,100,100]
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)