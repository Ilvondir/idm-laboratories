import pandas as pd

df = pd.DataFrame({
    "id": range(1, 5),
    "letters": ["a", "b", "c", "d"],
    "floats": [x / 2 for x in [3, 5, 7, 11]],
    "booleans": [True, False, False, True]
})

# Wyswietlenie calej ramki danych
print(df)

# Pobranie kolumny
print(df.letters)

# Pobranie wielu kolumn
print(df[["floats", "booleans"]])

# Pobranie pojedynczego wiersza
print(df.loc[2])

# Pobranie wielu wierszy
print(df.loc[[0, 2, 3]])

# Dodawanie i edytowanie wierszy
new_row = {
    "id": 5,
    "letters": "e",
    "floats": 8.5,
    "booleans": False
}
to_update = [6, "f", 10.2, True]
df.loc[len(df)] = new_row
df.loc[1] = to_update
print(df)

# Dodanie kolumny z wartosciami
new_column = [5, 4, 3, 2, 1]
df.insert(3, "added", new_column)
print(df)

# Usuniecie wiersza
df = df.drop(0)
print(df)

# Usuniecie kolumny
df = df.drop(columns=["floats"])
print(df)
