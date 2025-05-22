class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
    def ChangeCompany(self, newCompany):
        self.company = newCompany

e1 = Employee()
e1.name = "Bhavyansh"
e1.show()
e1.ChangeCompany("Tesla")
e1.show()