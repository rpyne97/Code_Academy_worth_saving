## Example 1 - most basic
# define the class as Musician
class Musician:
    title = "Rockstar" # class attribute title
drummer = Musician() # instantiate the class. drummer is now an instance of the the class Musician
print(drummer.title) # print out the drummer's title attribute, also a class variable

## Example 2 - add a method

class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles): # class method (function within a class)
        return miles * self.kms_in_a_mile

converter = DistanceConverter() # instantiate the class
kms_in_5_miles = converter.how_many_kms(5) # only pass one argument for miles because self is implicitly passed and refers to oject converter
print(kms_in_5_miles)

## Example 3 - __init__

class Circle:
    pi = 3.14
    # Add constructor here:
    def __init__(self, diameter):
        print('New circle with diameter: ' + str(diameter))

teaching_table = Circle(36)

## Explanation - class variable vs. instance variable
class Dog:

    kind = 'canine' # attribute kind is set to 'canine' and is therefore a class variable shared by all instances

    def __init__(self, name): # self references the object of the class
        self.name = name # instance variable unique to each instance

d = Dog('Fido') # note that you can call Dog and enter argument name without any class attribute
e = Dog('Buddy')
d.kind # 'canine' shared by all dogs
e.kind # 'canine' shared by all dogs

d.name # unique to the d instance
e.name # unique to the d instance

## Example 3 - 2 class methods
class Circle:
    pi = 3.14 # attribute pi set to 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:

        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius

# using __init__ method one does not need to include a class method call
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
# note that by using the self argument in circumference method, the pi class variable and the radius instance variable are accessed automatically
print(Circle.circumference(medium_pizza))
print(Circle.circumference(teaching_table))
print(Circle.circumference(round_room))
# alternatively, call circumference as an attribute of a pre-defined Circle class instance
# no argument needed because self creates a binding to the class variables and is able to access its radius attribute
print(medium_pizza.circumference())

# View class object's attributes
# Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores.
print(dir(medium_pizza))

## Example 4

class Student:
    # create a constructor by defining __init__() method. the mandatory self argument binds attributes to the Student class
    def __init__(self, name, year):
        self.name = name # save name parameter as an attribute
        self.year = year # save year parameter as an attribute
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def print_grades(self):
        for grade in self.grades:
            print grade.score
        return 1

# instances created from this class will be type <class '__main__.Grade'> and have the score attribute
class Grade:
    minimum_passing = 65 # class variable

    def __init__(self, score):
        self.score = score # self.score attribute

    def is_passing(self):
        if self.score >= Grade.minimum_passing:
            return True
        else:
            return False

# will print the class but not the acual grade value
print(Grade(100))
# Note Grade objects have a score attribute so you need to drill down to this level to print the score integer
print (Grade(100).score)

# instantiate Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# add the Grade of 100 to pieter instance .grades attribute
pieter.add_grade(Grade(100))
# now view the list of grades
pieter.print_grades()
# instantiate Grade class with a score of 60
pieter_grade = Grade(60)
#Test is this is a passing grade
pieter_grade.is_passing()
# False


