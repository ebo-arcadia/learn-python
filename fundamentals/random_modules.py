import random

for indx in range(10):
    print(random.random())
    print(random.randint(10,15))

memebrs = ["superman", "spiderman", "batman"]
lead = random.choice(memebrs)
print(lead)

# roll dice!
class Dice:
    def roll(self):
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        return (first_num, second_num)
    

dice = Dice()
print(dice.roll())