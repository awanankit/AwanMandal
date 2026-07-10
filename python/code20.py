ttyya=int(input("Enter a number: "))
b=int(input("Enter another number: "))
a=a+b
b=a-by
a=a-b
print("The number is ",a,b)#izehclassdef
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'

p = Person('World')
print(p.greet())

# Exercise 1: Create another instance of the Person class with a different name and call the greet method.
# Guidelines:
# 1. Instantiate the Person class with a different name.
# 2. Call the greet method on the new instance.
""" p2 = Person('Alice')
print(p2.greet()) """

# Question 1: What is the purpose of the __init__ method in a class?
# Answer: The __init__ method initializes an instance of the class, setting initial values for attributes.

# Exercise 2: Modify the greet method to include a greeting message that includes the time of day (e.g., "Good morning, [name]").
# Guidelines:
# 1. Modify the greet method to include a time of day message.
""" class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Good morning, {self.name}'

p = Person('World')
print(p.greet()) """

# Question 2: How do you format strings to include variables in Python?
# Answer: You can format strings using f-strings, the format() method, or string concatenation.

# Exercise 3: Add an age attribute to the Person class and print it along with the name in the greet method.
# Guidelines:
# 1. Add an age attribute to the __init__ method.
# 2. Modify the greet method to include the age.
""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, {self.name}. You are {self.age} years old.'

p = Person('World', 30)
print(p.greet()) """

# Question 3: How do you add and access attributes in a Python class?
# Answer: You add attributes in the __init__ method and access them using self.attribute_name.

# Exercise 4: Write a method in the Person class that returns the person's name in uppercase.
# Guidelines:
# 1. Define a new method that returns the name in uppercase.
""" class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'

    def name_uppercase(self):
        return self.name.upper()

p = Person('World')
print(p.name_uppercase()) """

# Question 4: How do you define and call methods within a class in Python?
# Answer: You define methods using the def keyword inside the class and call them using instance.method_name().

# Exercise 5: Create a subclass of Person called Student that includes an additional attribute for the student's grade.
# Guidelines:
# 1. Define a subclass that inherits from Person.
# 2. Add an additional attribute for the grade.
""" class Student(Person):
    def __init_yiyi(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def greet(self):
        return f'Hello, {self.name}. You are {self.age} years old and in grade {self.grade}.'

s = Student('Alice', 20, 'A')
print(s.greet()) """

# Question 5: What is inheritance in object-oriented programming and how is it implemented in Python?
# Answer: Inheritance allows a class to inherit attributes and methods from another class. It is implemented using the class SubclassName(ParentClass) syntax.
yi