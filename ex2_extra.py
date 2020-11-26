"""Moduł obsługi dodawania liczb palindromicznych
"""

# Liczby palindromiczne
#
# Liczba palindromiczna:
# 898 - Tak
# 1410 - Nie
# 9876789 - Tak
# 9 - Tak :)
#
# "Zabawne dodawanie"
# Dodajemy do liczby, odwróconą liczbę:
# 1410 + 0141 = ...
# 123 + 321 = ...
#
# Hipoteza:
# Po skończonej liczbie dodawań, zawsze otrzymamy wynik w postaci liczby palindromicznej.
# Hmm.. Sprawdź to dla zakresu [1, 190].
# W wyniku:
# Liczba: Ilość_dodawań Liczba_Palindromiczna
# ...
# 9: 0 9
# ...
# 12: 1 33
# ...
# int("1410")
# str(1410)
# int(str(1410)[::-1])

def is_palindrome_number(num):
    """Sprawdza czy liczba jest palindromiczna"""
    return int(str(num)[::-1]) == num

def funny_add(num):
    """Dodaje do liczby jej odwróconą pozycyjnie wartość"""
    return int(str(num)[::-1]) + num

def make_funny_adds(num):
    """Zwraca krotkę z (liczba, ilość dodawań, wartość końcowa)"""
    add_counter = 0
    result = num
    while not is_palindrome_number(result):
        add_counter += 1
        result = funny_add(result)
    return num, add_counter, result

def show_palindromic_numbers(min_val, max_val):
    """Prezentuje ilość dodawań palidromów w postaci -> Liczba: ilość_dodawań wynik_palindr"""
    for val in range(min_val, max_val + 1):
        print("%d: %d %d" % make_funny_adds(val))

if __name__ == '__main__':
    show_palindromic_numbers(1, 195)