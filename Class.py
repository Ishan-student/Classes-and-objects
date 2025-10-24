class name():
    def __init__(self,name,sirname):
        self.name=name
        self.sirname=sirname
    def fullname(self):
        print(f'{self.name}  {self.sirname}')
n1=name('Ishan','Maurya')
print(n1.name)
n1.fullname()
