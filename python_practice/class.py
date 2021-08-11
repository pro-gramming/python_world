# Working with concept of classes 
# The most important thing is the keyword self

class student:
  # defined special method
  # adding data or attributes to the class
  def __init__(self, first, last):
    # the name of the variables could be anything like self.(anything)
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@galgotias.com'

  # adding the actions based on the attributes i.e. funcions or method
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

stu_1 = student('dinesh', 'singh')
stu_2 = student('arush', 'kumar')

print("Print the email for the student:", stu_1.email)
print("Printing the full name of student:", stu_1.fullname())


# We could also call the function directly from the class but this time we 
# have to specify the instance like

print("calling directly from the class:",student.fullname(stu_2))

# or we could do this , below the self(positional argument is passed automatically)
print("calling using the instance with function name:",stu_2.fullname())
