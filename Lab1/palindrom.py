text = input("Podaj tekst: ")
_length = len(text)
half = _length // 2
palindrome = True

for i in range(0, half):
    if text[i].upper() != text[_length - 1 - i].upper():
        palindrome = False

if palindrome:
    print(f"'{text}' jest palindromem.")
else:
    print(f"'{text}' nie jest palindromem.")

