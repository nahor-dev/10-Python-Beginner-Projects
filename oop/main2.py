# class variable = shared among all instance(means objects ) define outside the constructor allow you to share data among all objects created from that class 


# class Car:
    #  wheels = 4  --> class variables 
    # def __init__(self,model,year):
        # self.model = model --> instance variable 
        
        


class Student:
    
    class_year = 2024  #--> class variables shared among all
    num_students = 0 
    
    def __init__(self,name,age):
        self.name = name  #--> instance variable do not shared among all 
        self.age = age
        # we want number of student to increment but we dont use self.num_students b/c self means just put student1 or student2 in place but for class variables we use the class name itself
        Student.num_students +=1
        
student1 = Student('bob' , 36)
student2 = Student('john' , 20)
student3 = Student('nah', 32)
student4 = Student('jah', 35)


print(student1.name)
print(student1.age)
print(student1.class_year)

print()
print(student2.name)
print(student2.age)
# when access class variable we need to access them with class name for clarity and readability 
print(Student.class_year)

print()

print(Student.num_students)

#  all in one 

print(f'my graduating class of {Student.class_year} has {Student.num_students}')
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)