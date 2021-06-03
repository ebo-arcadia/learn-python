class NewSampleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    
    def move(self):
        print("print move")
    
    def draw(self):
        print("print draw")


obj1 = NewSampleClass(123, 999)
obj1.attribute1 = 100
obj1.attribute2 = "nice"
print(obj1.attribute1)
print(obj1.attribute2)
obj1.draw()
obj1.move()

obj2 = NewSampleClass(20, 23)
print(obj2.x)
print(obj2.y)

class Person:
    def __init__(self, name):
        self.name = name
        pass
    
    def talk(self):
        print(f"{self.name} can talk!")
        

person1 = Person("Neo Anderson")
print(person1.name)
person1.talk()

person2 = Person("Devil Cry")
print(person2.name)
person2.talk()
