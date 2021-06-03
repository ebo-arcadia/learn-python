class Mammal:
    def walk(self):
        print("can walk")
        
class Dog(Mammal):
    def bark(self):
        print("bark!!!")


class Cat(Mammal):
    def mow(self):
        print("mow...")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.mow()
