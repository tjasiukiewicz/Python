# (1)
def slownie(numer):
    """Zamiana liczb na słowa w zakresie [0, 100)."""
    numer_napis = {
        0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć",
        6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć", 10: "dziesięć",
        11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście",
        15: "piętnaście", 16: "szesnaście", 17: "siedemnaście",
        18: "osiemnaście", 19: "dziewiętnaście", 20: "dwadzieścia",
        30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt",
        60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt",
        90: "dziewięćdziesiąt"
    }
    if numer > 99:
        return "ERROR!"
    elif numer in numer_napis:
        return numer_napis[numer]
    else:
        tens, rest = divmod(numer, 10)
        return numer_napis[tens * 10] + " " + numer_napis[rest]


print(slownie(33))


# (5)
def piramida(width):
    for stars in range(1, width + 1, 2):
        print(' ' * ((width - stars) // 2) + '*' * stars)


piramida(7)


# (3)
# "Na piechotę"
def sum_ascii(msg):
    sum_ = 0
    for i in msg:
        sum_ += ord(i)
    print(sum_)


sum_ascii("BILLGATES")


# Można szybciej :)
def sum_ascii(msg):
    print(sum(ord(c) for c in msg))


sum_ascii("BILLGATES")


# (2)
def ascii_table(min_value, max_value):
    for num, ch in enumerate(range(min_value, max_value + 1), min_value):
        print(num, chr(ch))


ascii_table(32, 127)


# (4)
def box(msg):
    bar = "*" * (len(msg) + 4)
    sep_bar = "* " + " " * len(msg) + " *"
    msg_box = "* " + msg + " *"
    print(bar, sep_bar, msg_box, sep_bar, bar, sep='\n')


box("Szkolenie z języka Python")
