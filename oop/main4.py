# multiple inheritance =  inherit from more than one parents class C(A,B)



class Prey:
    def flee(self):
        print('this animal is fleeing')
class Predator:
    def hunt(self):
        print('this animal is hunting ')


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass



rabbit  = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()
# rabbit.hunt() will give error b/c it dont have hunt method
hawk.hunt()
# hawk.flee()  will give error b/c it dont have flee method


# fish have both
fish.hunt()
fish.flee()




# multilevel inheritance = inheritance form a parent which inherits form another parents      C(B) <-- B(A)<-- A



class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f' {self.name} is eating')
    def sleep(self):
        print(f' {self.name} is sleeping')


class Prey(Animal):
    def flee(self):
        print(f' {self.name} is fleeing')
class Predator(Animal):
    def hunt(self):
        print(f' {self.name} is hunting ')


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass


rabbit  = Rabbit('bugs')
hawk = Hawk('tony')
fish = Fish('nemo')






rabbit.sleep()