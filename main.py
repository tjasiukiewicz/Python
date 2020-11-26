name = "Tomasz"
print(name)
name = 12
print(name)

# Referencje
a = 12   # a -> 12
b = a    # b -> a -> 12
b = 42   # b -> 42 , a -> 12
a = 11   # a -> 11, b -> 42, 12 kandydat do usunięcia przez GC

# Dwie kategorie typów
# Niemutowalne, Mutowalne
# Niemutowalne np.: liczby, stringi, tuple, ...
# Mutowalne np.: listy, dictionary, ...

name = "Tomasz"
name2 = name
name2 = "Adam"
name = "Zenon"

posilek = ["schabowy", "ziemniaki"]
posilek[0] = "kapusta"
print(posilek)
surowki = ["kapusta", "marchew"]
posilek[0] = surowki
print(posilek)
surowki[0] = "jabłko"
print(posilek)

uroburos = []
uroburos.append(uroburos)
print(uroburos)

data = [0, 1, 2]
data.append(data)
print(data)
print(data[3][1])

print(2**178)


napis = "abrakadabra"
print(napis[::-1])  # [początek:koniec:krok]
# [:] wszystkie
# [:4] do 3 włącznie (licząc od 0)
# [-4] od końca 4
# [::2] "co drugi"
# [::-1] kolejność odwrócona

slowo = "kajak"
print(slowo == slowo[::-1])

# Słownik
slownik = {"ala": 12, "tola": 15, "tomasz": 20}
print(slownik["ala"])
print(slownik.keys())
print(slownik.values())
print(slownik.items())

# Tuple
tpl = (12, "Jola", 123.4, [1, 2, 3], 34)
# tpl[0] = 42  # To jest błąd!
tpl[3][0] = 100
print(tpl)

print("Cześć. Nazywam się %s i mam %d." % ("Adam", 21))

# for (a = 12; a < 100; ++a) # Tego Python nie ma :)

data = [12, 33, 22, 44, 17]
for a in data:
    print(a)
    print("---")

for i in range(0, 11):
    print(i, end=', ')

print()

slownik = {"ala": 14, "tola": 65, "jola": 64}

for k, v in slownik.items():
    print("%s -> %d" % (k, v))

slownik["franek"] = 12
print(slownik)

for i, k in enumerate(slownik.keys()):
    print(i, k)

l1 = ['a', 'b', 'c']
l2 = [0,    10,  20]

for a, b in zip(l2, l1):
    print(a, b)

file = open("/etc/passwd", "r")
for line in file:
    print(line, end="")
file.close()

lineInMyFile = open("/etc/passwd", "r").readlines()  # Dyskusyjna praktyka
print(lineInMyFile[::-1])

data = {(0, 1): "tv", (10, 11): ["radio", "pen"], (22, 22): "desk"}
print(data[(22, 22)])

x = 1
y = 2
x, y = y, x
print(x, y)

# Liczby od 0 do n
n = 10
lst = []
for i in range(0, n):
    lst.append(i)

print(lst)

lst = [i * 10 for i in range(0, n)]
print(lst)

lst = [i * 10 for i in range(0, n) if i % 2 == 0]
print(lst)

# To będzie generator
lst_gen = (i * 10 for i in range(0, n) if i % 2 == 0)
print(lst_gen)
for i in lst_gen:
    print(i)

lst_gen = (i * 10 for i in range(0, n) if i % 2 == 0)
lst = list(lst_gen)
print(lst)

dct = {k: ord(k) for k in "abcdefgh"}
print(dct)

# Funkcje
def foo(a, b, c):
    print(a, b, c)

foo(1, "Honorata", 3)

def bar(a, b, c=10):
    print(a, b, c)

bar(1, 3)

def bar(a=1, b=12):
    print(a, b)

bar()

def foo(*args):
    print(type(args))
    for a in args:
        print(a)

foo(1, 2, 3)
foo()
foo("Ala", 12, 333, 23)

def foo(a, b, c=10, *args):
    pass

def foo(**kwargs):
    print(kwargs)

foo(host="127.0.0.1", login="hacker", passw="letmein")

print("a", "b", "b", sep="+")

def foo(a, b, c, d=12, e=45, *args, **kwargs):
    pass

def foo(myDict):
    print(myDict)

foo({"a": 123, "ala": 7877})

# map
prices = [100.0, 200.0, 500.0]

result = []
for price in prices:
    result.append(price * 1.23)

print(result)

result = [price * 1.23 for price in prices]

print(result)

def complex_tax(price):
    if 150.0 < price < 300.0:
        return price * 1.23
    return price * 1.07

result = []
for price in prices:
    result.append(complex_tax(price))

print(result)

result = map(complex_tax, prices)

print(list(result))

result = map(lambda p: 1.23 * p, prices)

print(list(result))

points = [(1, 2), (45, 2), (7, 8)]

print(list(map(lambda p: p[0] * p[1], points)))

dct = { "a": 1, "b": 2, "c": 12}
print(list(map(lambda k: str(k[0]) + str(k[1]), dct.items())))

#  Filter
data = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2, data)))

# Złożenie...
data = [1, 2, 3, 4, 5]
result = list(
    map(lambda x: x * 2,
        filter(lambda x: not (x % 2),
            data)
    )
)
print(result)

# reduce
from functools import reduce

# data = [ a, b, c ]
# X <- arg początkowy
# X a
#  +
#   X + a
#     X + a + b
#       X + a + c
data = [1, 2, 3]
result = reduce(lambda x, y: x + y, data, 10)
print(result)

# reduce nieco nietypowy
data = [1, 2, 3, 4, 5]

def count(counter, val):
    if val % 2:
        return counter + 1
    return counter

count_values = reduce(count, data, 0)
print(count_values)

# Oczywiście ten sam efekt
print(len(list(filter(lambda x: x % 2, data))))

print("-" * 30)

# Generator

def fibonacci():
    x0, x1 = 1, 1
    while True:
        yield x0
        x0, x1 = x1, x0 + x1

f = fibonacci()
for i in range(5):
    print(f.__next__())

def fibonacci(n):
    x0, x1 = 1, 1
    for _ in range(n):
        yield x0
        x0, x1 = x1, x0 + x1

for val in fibonacci(5):
    print(val)

# Argument domyślny jest instancjonowany w trakcie definiowania funkcji
class X:
    def __init__(self):
        print("Konstrukcja!")

def foo(x = X()):
    pass

def grow(x = []):  # Licznik dowiązań do x ma wartość 2. 1 to powiązanie ze zmienną, 2 zmienna jest używana w funckji.
    x.append(1)
    return x

print(grow())
print(grow())
print(grow(["ala", "tola"]))
print(grow())

# Krotka wywołań...

a, b, c = 1, 2, 3  # To są krotki. Mogę zapisać jawnie także tak....
(a, b, c) = (1, 2, 3)

k = (0)  # Python to "spłaszczy" do: k = 0
print(k)

k = (0,)  # O to jest krotka z 1 elementem
print(k)

#
#    X
#   /\
#   |
#   Y

class X:
    def show(self):
        print("In parent")

class Y(X):
    def show(self):
        X.show(self)
        print("In child")

y = Y()
y.show()

#    A
#  /\ /\
# B    C
# /\  /\
#   D

class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        super(B, self).show()
        #A.show(self)
        print("In B")

class C(A):
    def show(self):
        super(C, self).show()
        #A.show(self)
        print("In C")

class D(B, C):
    def show(self):
        super(D, self).show()
        #B.show(self)
        #C.show(self)
        print("In D")

d = D()
d.show()
print(d.__class__.__mro__)


