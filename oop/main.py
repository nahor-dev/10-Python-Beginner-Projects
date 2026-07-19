# object = a bundle of related attributes(variable/describe things/name) and method(functions/ what that thing does )  ex phone , cup,book   we need a class to create many objects 
# object --> phone 
# attribute --> version_num = 13  or is_on = true
# methods --> make-call, receive-call,turn-on,turn-off



# class = blueprint used to design the structure and layout of an object 




# then import it like this : from {name of file/module } import {name of class}


from car import Car

'''
# this is cut out and sent to new file 

class Car:  #car object capital letter in the first as convention
    def __init__(self, model, year , color , for_sale):  #this is constructor used in order to construct object / init means initialize self - this object is creating rn model , year ... car objects 
        self.model = model #to access the object we use self.object 
        self.year = year
        self.color = color
        self.for_sale = for_sale
'''

# to construct car object we need unique name that is car1 then car1 = Car() like function to invoke car object then provide equal number of argument self is provided automatically
car1 = Car('hellCut' , 2024, 'black', False)
car2 = Car('corvette' , 2025, 'blue', True)
car3 = Car('mustang', 2026, 'yellow' , True)

# print(car1)   <__main__.Car object at 0x000002860E696A50>   this will be the output that is the memory address of car object to access one of the attribute we write . then name of attribute . is known as attribute access operator

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

# when class take lot of space its handy to put them in new file 



car2.drive()
car1.stop()
car3.describe()