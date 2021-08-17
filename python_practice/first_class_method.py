''' First class function is a HIGHER order function that return 
    function or take function as it's argument '''


def html_tag(tag):
  
  def wrap_text(msg):
    print('<{0}>{1}</{0}>'.format(tag, msg))

  return wrap_text  # return the function without executing it

print_h1 = html_tag('h1')  # creating an object of html tag function
print_h1('Test Headline !')  # now providing the arguments 
print_h1('another test string')
