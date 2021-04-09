#Chinyere Sloley, ZZ34770

# Q1
import re

q1 = "ABCD+++1234+EFGH++****"

result = re.sub("\++", "-", q1)
print(result)


#Q2
q2 = [x**2 if x % 2 == 1 else 2 * x for x in range(1,31)]
print(len(q2), 'numbers in q2 list')
print(q2)


#Q3
str_list = ['UMBC', 'UMD', 'UMB', 'TU']

q3 = filter(lambda x: len(x) == 4, str_list)

print(type(q3))
print(list(q3))


#Q4
#Vehicle class
class Vehicle:

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    
    self._dict_ = {'make': self.make, 'model': self.model, 'year': self.year}

  def isNew(self):
    if self.year == 2021:
      return True
    else:
      return False


q4 = Vehicle('Honda', 'Accord', 2021)
print(type(q4))
print(q4._dict_)
print(Vehicle.isNew(q4))



#Q5
#SUV class
class SUV(Vehicle):

  def __init__(self, transmission, milage, *args, **kwargs):
    self.transmission = transmission
    self.milage = milage
    super().__init__(*args, **kwargs)
    self._dict_ = {'transmission': self.transmission, 'milage': self.milage, 'make': self.make, 'model': self.model, 'year': self.year}

q5 = SUV('Automatic', 75000, 'Honda', 'CRV', 2020)
print(type(q5))
print(q5._dict_)
print(SUV.isNew(q5))
