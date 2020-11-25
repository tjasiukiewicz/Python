# (5)
imie = 'rower'
imie = imie[:2] + 'b' + imie[-2:] + 't'
print(imie)

# (6)
fvat = {
    'sprzedawca': {
        'nazwa': "Kant & Oszust Sp. z o.o",
        'adres': "01-001 Kraków ul. Błotna 12",
        'NIP'  : "123123123123"
    },
    'kupujący'  : {
        'nazwa': "Wziąć i Uciekać S.A.",
        'adres': "03-003 Koluszki ul. Zachlapana 1",
        'NIP'  : "323323323323"
    },
    'pozycje'  : (
        {
          'nazwa': "Miś pluszowy",
          'netto': 50.5,
          'brutto': 62.11,
          'podatek': 11.61,
          'stawka_vat': 0.23
        },
        {
          'nazwa': "Łopata",
          'netto': 100.0,
          'brutto': 123.0,
          'podatek': 23.0,
          'stawka_vat': 0.23
        }
    ),
    'słownie': "szabanaście tysięcy szabandziesiąt złotych"
}

print(fvat["pozycje"][1]["nazwa"], fvat["pozycje"][1]["netto"])

# (7)
# Szachownica, podejście 1
row = [0] * 8
chessboard = [row] * 8
chessboard[1][2] = "King"

print(chessboard)
# Jak widać elementy się powtarzają i dostęp jest nieintuicyjny.

# Szachownica, podejście 2
chessboard = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(0)
    chessboard.append(row)
chessboard[1][2] = "King"

print(chessboard)
# Już lepiej, ale dalej nieintuicyjny dostęp

# Szachownica, podejście 3
chessboard = {}
for col_name in "abcdefgh":
    row = {}
    for row_num in range(8, 0, -1):
        row[row_num] = 0
    chessboard[col_name] = row

chessboard['e'][4] = "King"

print(chessboard)
# Dostęp lepszy, bo zgodny z notacją szachową

# Bonus, wybiega poza to co wiesz na tym etapie zajęć.... A można krócej?
chessboard = {
    col_name: {row_num: 0 for row_num in range(8, 0, -1)}
    for col_name in "abcdefgh"
}
chessboard['e'][4] = "King"

print(chessboard)
# I można nieco ładniej wyświetlić...
print()
from pprint import pprint
pprint(chessboard)