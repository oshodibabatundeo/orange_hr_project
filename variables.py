# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable na,e can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
# Variable names are Case-Sensitive - age, Age and AGE are three different variables.



a = 10          #  x is of datatype integer - int
a = "Confix"    # x is now of datatype -  str
print(a)

print()

#Casting - specifying the data type of a variable can be done by casting
# x = str(3)      # x will be '3'
# y = int(3)      # y will be 3
# z = float(3)    # z will be 3.0
# print(x)
# print(y)
# print(z)
# print()
# print(f"{x}\n{y}\n{z}")

print()

#Getting the datatype of a variable - type() function
b = 5
k = "Henry"
print(type(b))
print(type(k))

# Declaring/Naming variables in pythin is Case Sensitive
g = 4
G = "John"
#In this program, G will NOT overwrite g because they are two different variables

#Camel Case - Each word, except the first, starts with a capital letter
confixHub = "Automation Class"

#Pascal Case - Each word starts with a capital letter
ConfixHUb = "HenryOkolie"

#Snake Case - Each word is separated by an underscore character
confix_hub = "John"

print()

#Unpacking a list
fruits = ["Grapes", "Oranges", "Pawpaw"]
x, y, z,  = fruits
print(x)
print(y)
print(z)





