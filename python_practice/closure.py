''' Closure is property of function to remember the 
    value of FREE variable in the scope in which it was
    created '''

# Example is as follows:

def outer_func():
  message = 'Hi'

  def inner_func():
    print(message)

  return inner_func

my_func = outer_func()

print(my_func.__name__)
print(my_func)
print(my_func())
