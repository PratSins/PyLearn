class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal  ---> changes salary as both object attribute and class attribute
    #     self.salary = sal    ---> changes salary as both object attribute only

    @classmethod
    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
