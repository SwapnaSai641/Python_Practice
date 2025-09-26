#Inheritance

#Simple inheritance
class Animal:
    def sound(self):
        print('The animal makes sound')

class Dog(Animal):
    def bark(self):
        print('The Dog barks')

# dog=Dog() #here dog is the child class object accessing parent class method sound()
# dog.sound() #The animal makes sound
# dog.bark() #The Dog barks

#Multiple inheritance
class Animal:
    def sound(self):
        print('The animal makes sound')

class mammal:
    def feed(self):
        print('It feeds milk to their babies')

class Dog(Animal,mammal):
    def bark(self):
        print('The Dog barks')

# dog=Dog()
# dog.sound()
# dog.feed()

#Multilevel

class Animal:
    def sound(self):
        print('The animal makes sound')

class mammal(Animal):
    def feed(self):
        print('It feeds milk to their babies')

class Dog(mammal):
    def bark(self):
        print('The Dog barks')

# dog=Dog()
# dog.sound()
# dog.feed()

#Heirarchial
class Animal:
    def sound(self):
        print('The animal makes sound')

class Dog(Animal):
    def bark(self):
        print('The Dog barks')

class Cat(Animal):
    def drink(self):
        print('Cat drinks milk')

dog=Dog()
dog.sound()
dog.bark()

cat=Cat()
cat.sound()
cat.drink()
