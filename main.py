# El siguiente archivo contiene una secuencia de instrucciones sin relación las unas con las otras.
# El objetivo de desarrollar este código es aprender a programar en python.

# Hello world.
print('Hola')

# Numbers.
print(2 + 2)
width = 20
height = 5 * 9
print(width*height)
tax = 17.5/100
print(tax)

# Strings.
s = 'terrance'
print(s)
print(s[2], s[0:2], s[2:4], s[1:], s[-1:], s[2:])
print(s + ' said', 'tax:' + str(tax))

# Lists.
a = ['terrance', 'filip', 'buba', 100, 1234]
print(a)
print(len(a))
a.append(2323)
print(a)

# Tuples.
t = (1, 2, 'Pedro')
print(t[2])

# Dictionaries.
tel = {'terrance': 5550, 'filip': 666, 'homer': 777}
print(tel)
print(tel['homer'])
tel['pedro'] = 777
print(tel)
print(tel.keys())
# print(tel.has_key('homer'))       # No es reconeix el mètode has_key().

# Commands and expressions.

# Conditionals.
# x = int(raw_input("Enter a number: "))        # No es reconeix el mètode raw_input().
x = 26
print(x)
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Loops.
x = 0
while x < 5:
    print(x)
    x += 1
a = ['cat', 'window', 'defenestrate']
for x in a:
    print(x, len(x))
print(range(10))        # S'imprimeix 'rang(0, 10)'. No s'imprimeix tot el rang.
print(range(5, 10))     # S'imprimeix 'rang(5, 10)'. No s'imprimeix tot el rang.
for i in range(9, 1, -1):
    print(i)

# Functions.
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b
fib(2000)
f = fib
f(100)
def add(x, y = 10):
    return x + y
print(add(5, 6))
print(add(5))
id = lambda x: x
print(id(5))
def make_incrementor(n):
    return lambda x, incr = n: x + incr
x = make_incrementor(2)
print(x(3))

# Functional programming.
numbers = [1, 2, 3, 4, 5]
def incr(x):
    return x + 1
map(incr, numbers)      # La única cosa que s'aconsegueix imprimir de la funció map() és l'adreça de memòria.
map(len, ["one", [2, 3]])
map(str, numbers)
# print(reduce(lambda x, y: x + y, numbers))      # No es reconeix la funció reduce().
filter(lambda x: x % 2 == 0, numbers)
[x + 1 for x in numbers if x % 2 == 0]      # No em queda clar l'apartat de programció funcional.

# Classes and OOP.
class Thing:
    name = 'cosa'
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def __repr__(self):
        return 'Thing(' + self.name + ')'
c = Thing()
print(c.name)
print(c)
c.name = '666'
print(c)
class Other:
    def __init__(self, x):
        self.name = x
c = Other('Pedro')
print(c.name)
class Private:
    # We cannot access a private var from outside the class.
    __mine = 'hola'
c = Private()

# Inheritance.
class Animal:
    def talk(self):
        print('I am an animal')
class Dog:
    def talk(self):
        print('I am a dog')
class Cat:
    def talk(self):
        print('I am a cat')
a = Animal()
d = Dog()
c = Cat()
farm = [a, d, c]
for animal in farm:
    animal.talk()
class Mouse(object):
    def talk(self):
        print('I am a mouse')
class Rat(Mouse):
    def talk(self):
        super(Rat, self).talk()
r = Rat()
r.talk()

# Duck typing.
class Mutant:
    def talk(self):
        print('I am a mutant')
farm.append(Mutant())
for animal in farm:
    animal.talk()

# Files.
f = open('output.txt', 'w')
f.write('1 2 3 4 5 6 \n')
f.write('7 8 9 10 11 \n')
f.write('12 13 14 15 16 \n')
f.close()
f = open('output.txt')
lines = [line.split() for line in f.readlines()]
f.close()
print(lines)