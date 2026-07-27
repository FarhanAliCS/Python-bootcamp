class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def display(self):
        print("car name :",self.name)
        print("car model :",self.model)

car1=Car('honda civic',2026)
car1.display()