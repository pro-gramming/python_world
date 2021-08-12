class Employee:
  
  # Specifying the class variables below:

  num_of_emps = 0  # this one will remain constant across all instances 
  raise_amount = 1.04  # a const amt used by all instances 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.num_of_emps += 1  # amt inc when a new instance in created 

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount) 

    ''' in above line we are using self.raise_amount , meaning 
        first the variable is checked in the scope of instance 
        if it exists , then its value is used ,IF NOT exist then
        it find the class from which it is inheriting the variable
        from '''


# To get the list of the attribute and the methods names of a instance or a class
#print(Employee.__dict__)


# Below code to cross-check the above concept

print("before creating two emp's", Employee.num_of_emps)

emp_1 = Employee('Dinesh', 'Singh', 5000000)
emp_2 = Employee('Aarush', 'lola', 5000000)

print("After creating two employees",Employee.num_of_emps)


