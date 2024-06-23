#The function deletes the named attribute, provided the object allows it.

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')

print(Person.country)
