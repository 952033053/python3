class Animal:
    def shout(self):
        print("喊叫")


class Bird(Animal):
    def fly(self):
        print("飞")


class Dog(Animal):
    def run(self):
        print("跑")


animal = Animal()
bird = Bird()
dog = Dog()
print(isinstance(Animal, Bird))
print(isinstance(dog, Animal))

print(issubclass(Dog, Bird))
print(issubclass(Dog, Animal))
