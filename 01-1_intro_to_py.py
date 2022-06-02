# %%
# Print Hello World

print("Hello World")

# Variable are declared without specifying types
a = 4
b = -5
print(a + b)
# %%
# The type of a variable is automatically determined
a1 = 4
a2 = "4"
print(type(a1))
print(type(a2))

# In Python, a string can be define using either "" or ''
str1 = "Wednesday"
str2 = 'Wednesday'
print(str1)
print(str2)
# %%
str3 = 'Someone said "Hey!"'
str4 = "Someone said 'Hey!'"
print(str3)
print(str4)

# Other commonly-used types are float and boolean
c = 1.5
d = True
print(type(c))
print(type(d))
# %%
# Variable types can be changed like this:
float_a = float(a)
a_as_a_float = float(b)

# Exercise: show the variable type of float_a

print(type(float_a))
print(type(a_as_a_float))

# +, -, *, /
# // -> integer division
print(4 / 3) # gives a floating point number
print(4 // 3) # integer division always give an integer as answer

# % -> Get remainder from integer division
print(5 % 3) 

# Using % 10, you can extract the last digit of a number.
a = 239542
print(a % 10)

# ** -> powers
print(3 ** 2) # represents 3 to the power of 2 = 9
print(4 ** (1/2)) # square root of 4
# %%
# Use quadratic formulat to solve equation x**2 - 5x + 4 = 0
a = 1
b = -5
c = 4

disc = (b**2 - 4*a*c) ** (1/2) # sqrt(b^2-4ac)
x1 = (-b - disc) / (2*a) # (-b-disc)/2a
x2 = (-b + disc) / (2*a) # (-b+disc)/2a

print(x1, x2)

a = 1
a += 1 # a = a + 1
print(a)

b, c, d = 2, 3, 4
b -= 5 # updates b value 2-5 = 3
c *= 10 # updates c value 3*10 = 30
d /= 2 # updates d value 4/2 = 2
print(b, c, d)
# %%
t, f = True, False
print(t, f)

print(True or False) # "or" means or
print(True and False) # "and" means and
print(not True)
print(not False)

# Comparisons: >, <, ==, !=, >=, <=
exp1 = (a > 5) and (b < 3)
print(a, b, exp1)
# %%
str1 = "Hello"
str2 = 'World'
str3 = '3'
print(type(str3))
print(str1 + str2 + str3) # Use "+" to concatenate strings
print("My \n Name \n Is \t Liang.")
print('I said "Good Morning"') # If the string contains "", then use '' to define the string
print("I said \"Good Morning\"")

# Remove extra space at the beginning and the end of a string
data_value = "     Liang Zhao     "
my_name = "Liang Zhao"
print(data_value == my_name)
print(data_value.strip())
print(data_value.strip() == my_name)

# Split a string
file_names = "Alex, Bob, Clare, David"
file_names.split(", ")

# String formatting
float_num = 45.67898765
print(float_num)
print("%5.2f" % (float_num))
print("%08.2f" % (float_num))
formatted_string = "Name: %10s | Score: %5d | Value: %.2f" % ("Alex", 89, 12.345)
print(formatted_string)
formatted_string = "Name: %10s | Score: %5d | Value: %.2f" % ("Bob", 9, 543.21)
print(formatted_string)
# %%
# List
list1 = [1, 2, 3, 4, 6.5, "Monday", True]

print(list1)
list1.append(12)
print(list1)

val = list1.pop()
print(val)
print(list1)

# Indexing
print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-2])
print(list1[2:5]) # the second index is exclusive
print(list1[:5]) # omitting the first index means starting from 0
print(list1[2:]) # omitting the second index means going to the end
print(list1[:]) # prints out everything

len(list1)

# Set
set1 = {1, 2, 3, 3, 2, 1}
print(set1)

# Tuple - cant be changed
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 1)
print(tuple1 == tuple2)

# Dictionary: (key, value)
dict1 = {"Alex": "A",
         "Bob": "B", 
         "Clare": "C"}
print(dict1['Alex'])
print(dict1['Clare'])
# %%
names = ['Alex', 'Bob', 'Clare']
for name in names: # for (variable) in (list of values):
    print(dict1[name]) # Use indentation (4 spaces) to indicate the loop body

for name in names:
    # just print the names
    print(name)

a = 2
if a > 0:
    print("Greater than zero.")
else: 
    print("Not greater than zero.")

a = 2
b = 4
if a < 0:
    print("a less than zero")
elif b > 0: # "elif" means "else if"
    print("a not less than zero, and b greater than zero")
else:
    print("neither is greater than zero")


# %%
def sum_of_list(list1):
    sum = 0
    for x in list1:
        sum += x
    return sum

list1 = [1,3,4,5]
sum_of_list(list1)

# Exercise: Create a funtion that finds the maximum value of a list
def find_maximum(list1):
    return max(list1)
find_maximum(list1)


# %%
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person object created.")

    def print(self):
        print("Name:", self.name, " | Age: ", self.age)

alice = Person("Alice", 25)
alice.print()

class Student(Person):

    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        print("Student object created.")

    def print(self):
        super().print()
        print("ID: ", self.id)

alice = Student("Alice", 25, 12345)
alice.print()


# %%
# A list of student names and a list of students scores are given as follows:
names = ['Alice', 'Bob', 'Clare', 'David', 'Edward', 'Frank', 'Gabriel']
scores = [99, 88, 77, 66, 55, 44, 33]

def find_average(scores):
    return sum(scores) / len(scores)
find_average(scores)

def who_failed(names, scores):
    failed = []
    for i, v in enumerate(scores):
      if v < 65:
        failed.append(names[i])
    return failed
who_failed(names, scores)

def get_letter_grades(scores):
    letter = []
    for i, v in enumerate(scores):
        if 90 <= v:
            letter.insert(i,"A")
        elif 80 <= v:
            letter.insert(i,"B")
        elif 70 <= v:
            letter.insert(i,"C")
        elif 60 <= v:
            letter.insert(i,"D")
        else:
            letter.insert(i,"F")
    return letter
get_letter_grades(scores)
# %%
