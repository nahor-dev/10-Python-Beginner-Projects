class Car:  #car object capital letter in the first as convention
    def __init__(self, model, year , color , for_sale):  #this is constructor used in order to construct object / init means initialize self - this object is creating rn model , year ... car objects 
        self.model = model #to access the object we use self.object 
        self.year = year
        self.color = color
        self.for_sale = for_sale
# methods are actions objects can perform 


    def drive(self):
        print(f'you drive the {self.color} {self.model}')
    def stop(self):
        print(f'you stop the {self.color} {self.model}')
    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
        