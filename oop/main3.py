# inheritance = allows a class to inherit attributes and methods from another class help with code readability and extensibility class child (parent )
# like child inherits habits from parents 

# class Father :
#     height = 182
#     color = 'pink'
# class Son(Father):
#     pass-



class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')
class Dog(Animal):
    def speak(self):
        print('woof')
class Cat(Animal):
    def speak(self):
        print('meow')
class Mouse(Animal):
    def speak(self):
        print('squeek')


dog = Dog('bob')
cat = Cat('garfield')
mouse = Mouse('mickey')


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
print(cat.name)
print(mouse.name)