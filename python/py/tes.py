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
    

    
emp_1 = Employee('victor', 'kinoti', 45000)
emp_2 = Employee('Caroline', 'Mwadzoya', 50000)
emp_3 = Employee('Daisy', 'Memo', 78000)

emp_str_1 = 'florence-mjaka-90000'
emp_str_2 = 'joy-Mbithe-100000'
emp_str_3 = 'esta-mugs-200000'

new_emp_1 = Employee.from_string(emp_str_3)


print(new_emp_1.email)
print(emp_2.apply_raise())

