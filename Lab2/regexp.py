import re

main_text = "40-letni tata Ali umowil sie z nami na 21.30"

# findall - znajduje wszystkie wystapienia wyrazenia w tekscie
pattern = "[0-9]+"
res = re.findall(pattern, main_text)
# print(res)

# split - dzieli tekst na podstawie wystapienia wyrazenia regularnego
pattern = "[aeoiu]"
res = re.split(pattern, main_text)
# print(res)

# sub - zamienia wystapienia wyrazenia regularnego na inny tekst
pattern = "[0-9]"
res = re.sub(pattern, "?", main_text)
# print(res)

# search - wyszukuje pierwsze wystapienie wyrazenia
pattern = "Ali"
res = re.search(pattern, main_text)
# print(res)

# match - sprawdza, czy wzorzec pasuje do początku ciagu znakow
pattern = "30"
res = re.match(pattern, main_text)
# print(res)

# fullmatch - sprawdza, czy caly ciag znako pasuje do wzorca
pattern = r"[a-zA-Z0-9-\s.]+"
res = re.fullmatch(pattern, main_text)
# print(res)

# finditer - znajduje wszystkie dopasowania wzorca w ciagu znakow jako iterator
pattern = "[A-Z]"
res = re.finditer(pattern, main_text)

# for m in res:
#     print(m)

# escape - unieszkodliwia znaki specjalne
res = re.escape(main_text)
print(res)