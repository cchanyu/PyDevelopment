# Integer, String
print(5)
# 5

print(-10)
# 10

print(3.14)
# 3.14

print(5+3)
# 8

print(2*8)
# 16

print(3*(3+1))
# 12

print('Balloon')
# Balloon

print("Butterfly")
# Butterfly

print("ha"*9)
# hahahahahahahahaha

# Boolean: True / False
print(5 > 10)
# False

print(10 > 5)
# True

print(True)
# True

print(not True)
# False

# Introducing an animal
name = "YonTan"
animal = "Dog"
age = 4
hobby = "talking a walk"
is_adult = age >= 3

print(name + " is a " + animal + " in my house.")
print(name + " likes to " + hobby + " and he's " + str(age) + " years old")
print("Is " + name + " an adult? " + str(is_adult))

# this is one line comment
''' this is 
multiple lines
of commands '''

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # leftover after division = 2
print(10%3) # leftover after division = 1
print(5//3) # 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # False
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)

number = number + 2 # 16
print(number)

number += 2 # 18
print(number)

number *= 2 # 36
print(number)

number /= 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 2 # 0
print(number)

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # finds the max value, 12
print(min(5, 12)) # finds the min value, 5
print(round(3.14)) # round up number, 3 
print(round(4.99)) # round up number, 5

from math import *
print(floor(4.99)) # round down / drop digits, 4
print(ceil(3.14)) # round up always, 4
print(sqrt(16)) # square root, 4

from random import *
print(random()) # random number between 0.0 - 1.0
print(random() * 10) # random number between 0.0 - 10.0 
print(int(random() * 10)) # random number between 0 - 10
print(int(random() * 10) + 1) # random number between 1 - 10

print(randrange(1, 46)) # random number between 1 - 46
print(randint(1, 45)) # random number between 1 - 45

sentence = "I'm a teenager"
print(sentence)
sentence2 = "python is easy"
print(sentence2)
sentence3 = """
what is up
python is easy
"""
print(sentence3)

# Slicing
jumin = "990120-1234567"
print("gender : " + jumin[7]) #1
print("year: " + jumin[0:2]) #99
print("month: " + jumin[2:4]) #01
print("birthdate: " + jumin[:6]) #990120
print("last 7 digits: " + jumin[7:]) #1234567
print("last 7 digits in reverse: " + jumin[-7:]) #[-7] = 1 -> 1234567

python = "Python is amazing"
print(python.lower()) # lowercase
print(python.upper()) # uppercase
print(python[0].isupper()) # is Python[0] = P an upper? T/F = T
print(len(python))
print(python.replace("Python", "Java")) # replaces word Python to Java

index = python.index("n") # finds n's locations in the sentence
print(index)
index = python.index("n", index + 1) # finds the next n location
print(index)

print(python.find("n")) # finds word location in the sentence
print(python.find("Java")) # will return -1 cause can't be found
# print(python.index("Java")) # will return an error

print(python.count("n")) # 2 n's found = 2


# Format by Text
print("I'm %dyears old." %20) # %d means = int. it'll print 20.
print("I like %s." % "Python") # %s means = string, it'll print str
print("Apple starts with %c" % "A") # %c means = character, it'll print 1 char
print("I like %s and %s colors" % ("blue","red")) 

print("I'm {}years old".format(20)) # I'm 20 years old
print("I like {} and {} colors".format("blue","red"))
print("I like {1} and {0} colors".format("blue","red")) # 0 = blue, 1 = red

print("I'm {age} years old, I like {color} color".format(age=20, color="red"))
age = 20
color = "red"
print(f"I'm {age} years old, I like {color} color")


print("one in a\n lifetime") # \n = new line
print("I'm 'Chanyu'desu")
print("I'm \"Chanyu\"desu")

# \\: when u want to print \ 
print("C:\\Users\\Coding") # C:\Users\Coding

# \r: moves to the front cursor
print("Red Apple\rPine") # PineApple Pine moves to 0 spot

# \b: backspace (deletes 1 letter)
print("Redd\bApple") # deletes 1 letter before

# \t: tab
print("Red\tApple")


# LIST
subway = [10, 20, 30]
print(subway)

