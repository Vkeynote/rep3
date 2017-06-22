class Employee:
    raise_amount = 1.04
    num_of_emps = 0
   
    
    def __init__(self , first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
       first, last, pay = emp_str.split('-')
       return cls(first, last, pay)
    

class Developer(Employee):
    raise_amount = 1.70

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
            
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

        
dev_1 = Developer('Vik', 'Keynote', 100000, 'python')
mgr_1 = Manager('Kinoti', 'Kiambi', 500000, [dev_1])

print (mgr_1.fullname())
print(mgr_1.email)


