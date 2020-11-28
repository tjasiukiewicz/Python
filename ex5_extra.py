# Parsowanie i liczenie ilości wystąpień wyrazów w pliku tekstowym

from collections import Counter

def most_common_words(file_name, count):
    counter = Counter()
    file = ''
    try:
        file = open(file_name, "r", encoding="UTF-8")
        for line in file:
            counter.update(line.split())
    except FileNotFoundError as e:
        print(e)
        raise RuntimeError("Missing file!!!")
    return counter.most_common(count)

# Stosując zarządcę kontekstu...
def most_common_words2(file_name, count):
    counter = Counter()
    try:
        with open(file_name, 'r', encoding="UTF-8") as file:
            for line in file:
                counter.update(line.split())
    except FileNotFoundError as e:
        print(e)
        raise RuntimeError("Missing file!!!")
    return counter.most_common(count)


# .. i zapis z wyrażeniem generatorowym
def most_common_words3(file_name, count):
    counter = Counter()
    try:
        with open(file_name, 'r', encoding="UTF-8") as file:
            [counter.update(line.split()) for line in file]
    except FileNotFoundError as e:
        print(e)
        raise RuntimeError("Missing file!!!")
    return counter.most_common(count)


if __name__ == '__main__':
    for c, count in most_common_words3("tadeusz.txt", 10):
        print(c, count)