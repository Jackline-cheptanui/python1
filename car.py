class Car:
    type="BWM"

    def __init__(self,name,color):
       self.name=name
       self.color=color


    def model(self):
        return f"my car name is {self.name}"
    def apearance(self):
        return f"car color is{self.color}"
        
