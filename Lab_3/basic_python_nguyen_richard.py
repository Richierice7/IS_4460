#Part 1: Comments
#My first comment!

#Part 2: Literals
print("Darth Vader") #this is an object
print(4.0) #this is a float

#Part 3: Variable Names
d = 6
D = 16
print(d)
print(D)

#Part 4: Strings and Variables
character_name = "Darth Vader"
character_gpa = 1.4
print(character_name)
print(character_gpa)

print("My name is " + character_name + " not Luke")

print(f"My name is {character_name} not Luke")

#Part 5: Converting between types
num  = 432134/34
print(str(num)[1:5])

#Part 6: a,b function
def multiply_num(a,b):
  output = a*b
  return output

print(multiply_num(4,5))
print(multiply_num(b = 32,a = 21))

#Part 7: say_hello function
name = "Bobby"

def hello_world():
  name = "Eddy"
  print(name)

hello_world()

for count in range(0,20):
  print([count])