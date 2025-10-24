class name():
    def __init__(self,name,sirname):
        self.name=name
        self.sirname=sirname
    def fullname(self):
        print(f'{self.name}  {self.sirname}')
n1=name('Ishan','Maurya')
print(n1.name)
n1.fullname()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def show_details(self):
        return [f"{self.year} {self.make} {self.model}"]
# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.show_details())  # Output: 2020 Toyota Corolla
