class Employee:

  raise_amount = 1.04  # a const amt used by all instances 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'


  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount) 


# Functions like __init__ are special methods that whose names are already occupied
# and there way of utilization is also specified like __add__ function and so on.

  def __repr__(self):    # repr and str special methods alongwith init should be used always
    return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

  def __str__(self):    
  # if str is not specified within the class, and is still used on the object
  # then the default behaviour is to fallback to the repr special method
    return '{} - {}'.format(self.fullname(), self.email)

  def __add__(self, other):
    return self.pay + other.pay

  def __len__(self):
    return len(self.fullname())

emp_1 = Employee('Dinesh', 'Singh', 5000000)
emp_2 = Employee('Aarush', 'lola', 5000000)

print('printing the length of the object fullname', len(emp_1))

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

