class Employee:

  num_of_emps = 0  
  raise_amount = 1.04  

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.num_of_emps += 1  

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount) 

  # defining the classmethod to work with class attributes  ( not instances)
  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount

  # defining the classmethod as an alternative constructor:
  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  # defining the staticmethod to check if the day is working day or not:
  @staticmethod
  def is_workday(day):
    if day.weekday() == 7 or day.weekday() == 6:
      return False
    return True


# Checking the above concept of classmethods:

emp_1 = Employee('Dinesh', 'Singh', 5000000)
emp_2 = Employee('Aarush', 'lola', 5000000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# sample examples to check the working of alternative constructor:

emp_str_1 = 'Dinesh-Singh-834746'
emp_str_2 = 'Chandrakant-Kumar-927252'

new_emp_1 = Employee.from_string(emp_str_1)

print("Printing the values after applying the classmethod as an alternative constructor")
print("Print email of new_emp_1", new_emp_1.email)
print("Print pay of new_emp_1", new_emp_1.pay)


# Code to check the staticmethod:

import datetime
my_date = datetime.date(2021, 8, 12)

print("Is {} is weekday or not: {}".format(my_date, Employee.is_workday(my_date)))

