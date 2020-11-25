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
print(napis[::-1]) # [początek:koniec:krok]
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
#tpl[0] = 42  # To jest błąd!
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

lineInMyFile = open("/etc/passwd", "r").readlines() # Dyskusyjna praktyka
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