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

# Here creating the another class that will inherit Employee class

class developer(Employee):
  raise_amount = 1.10   # specifying it owns raise amount 

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)  
    # let employee init method to deal with initialization 
    # first last and pay variables to make the code maintianable and easy to read
    # OR we can do something like: Employee.__init__(self, first, last, pay)

    self.prog_lang = prog_lang  # from developer class

''' some questions to answer:
    what will happen if you just create developer class and initiate its instance 
    without specifying anything in that class
like: 

  class developer(Employee):
    pass

dev_1 = developer('Dinesh', 'Singh', 500000)
'''



# creating one more class 

class manager(Employee):

  def __init__(self, first, last, pay, employees=None):  # mutuable data type should not be pass here like list
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


  def print_emps(self):
    for emp in self.employees:
      print('-->', emp.fullname())

dev_1 = developer('Dinesh', 'Singh', 500000, 'Python')
dev_2 = developer('Aarush', 'Singh', 400000, 'java')

# print(dev_1.pay)


#print(dev_1.email)
#print(dev_1.prog_lang)

mgr_1 = manager('Dada', 'Dinesh', 9276034098, [dev_1])
print('email of manager:', mgr_1.email)
print('printing the employee this manger supervises:')
mgr_1.print_emps()



# TWO important functions to check if the object is instance of particular class:
print('checking using isinstance()', isinstance(mgr_1, manager))

# checking is a class is a subclass of another:
print('checking using issubclass()', issubclass(manager, Employee))
