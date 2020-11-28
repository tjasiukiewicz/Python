# Szukanie liczb doskonałych

def proper_dividers(value):
    dividers = []
    for i in range(1, value):
        if value % i == 0:
            dividers.append(i)
    return dividers


print(proper_dividers(6))


# Ale może nieco nowocześniej i ... wydajniej? Po co dzielić przez elementy powyżej value // 2?
def proper_dividers(value):
    """Zwraca listę dzielników właściwych liczby"""
    return [divider for divider in range(1, value // 2 + 1) if value % divider == 0]


print(proper_dividers(6))


def is_perfect_number(value):
    """Predykat sprawdzający czy liczba jest doskonała"""
    return sum(proper_dividers(value)) == value


def perfect_number_in_range(min_value, max_value):
    """Zwraca z zakresu [min, max], liczby doskonałe"""
    result = []
    for val in range(min_value, max_value + 1):
        if is_perfect_number(val):
            result.append(val)
    return result


# Generator z kodu "w stylu C"
def perfect_number_in_range_gen(min_value, max_value):
    """Generator zwracający z zakresu [min, max], liczby doskonałe"""
    for val in range(min_value, max_value + 1):
        if is_perfect_number(val):
            yield val


for val in perfect_number_in_range_gen(1, 11000):
    print(val)


print(perfect_number_in_range(1, 100))


# Nie no.. nowocześniej!
def perfect_number_in_range(min_value, max_value):
    """Zwraca z zakresu [min, max], liczby doskonałe"""
    return [val for val in range(min_value, max_value + 1) if is_perfect_number(val)]


print(perfect_number_in_range(1, 10000))


def perfect_number_in_range_gen(min_value, max_value):
    """Generator zwracający z zakresu [min, max], liczby doskonałe"""
    return (val for val in range(min_value, max_value + 1) if is_perfect_number(val))


for val in perfect_number_in_range_gen(1, 11000):
    print(val, flush=True)


# Rozwiązanie ostateczne
def is_perfect_number(value):
    """Predykat sprawdzający czy liczba jest doskonała"""
    return sum(proper_dividers(value)) == value


def is_perfect_number(value):
    """Predykat sprawdzający czy liczba jest doskonała"""
    return sum(proper_dividers(value)) == value


def perfect_number_in_range(min_value, max_value):
    """Zwraca z zakresu [min, max], liczby doskonałe"""
    return (val for val in range(min_value, max_value + 1) if is_perfect_number(val))


# Ocztwiście rozwiązać zadanie można także z wyrażeniem generatorowym "w całości"
# Tylko czy to jest czytelne? :/
def perfect_number_in_range_gen2(min_value, max_value):
    return (val for val in range(min_value, max_value + 1) if sum(
                divider for divider in range(1, val // 2 + 1) if val % divider == 0
            ) if sum(proper_dividers(val)) == val
    )


for val in perfect_number_in_range_gen2(1, 11000):
    print(val)
