import math

def dollarizer(word: str):
   x = word.replace("s","$")
   print(x)
   return x

def eurizer(word: str):
   x = word.replace("e","*")
   return x

def replacer(word: str, char1: str, char2: str):
   x = word.replace(char1, char2)
   return x


def wonky_text(word: str):
   x = eurizer(word)
   y = dollarizer(x)
   z = replacer(y,"i","z")
   return z


def celcius_to_fahrenheit(temp: float):
   f = temp * (9/5) + 32
   return f

def age_in_days(age: int):
   days = age * 365
   return days

def simple_interest(principal: int, interest_rate: float, year: int):
   simple_interest = principal * interest_rate * year
   return simple_interest

def plan_finances(p: int, r: float, years: int, f: float):
   if (f == p*r*years):
      return True
   else:
      return False
   
def rectanlge(l: int, w: int):
   area = l*w
   return area

def circle(r: int):
   area = math.pi *r**2
   return area

def trinagle(base: int, height: int):
   area = 0.5 * base * height
   return area

def square_perimeter(side: int):
   perimeter = 4* side
   return perimeter

def circle_details(r: int):
   circumference = math.pi * 2 * r
   print(f"The area of the circle is {circle(r)} and the perimeter is {circumference}")
   return circumference

def geometry(side: int, r: int):
   if (square_perimeter(side) < circle_details(r)):
      print(f"Circle has a larger perimter")
   else:
      print(f"Square has a larger perimeter")
   if ( side**2 < circle(r)):
      print(f"Circle has a larger area")
   else:
      print(f"Square has larger area")

geometry(8, 3)
#print(wonky_text("sssooocooolssssiiiiiooooeeeeee"))