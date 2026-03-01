s = input("Enter a string: ")
vowels = 0
if s.lower() == s[::-1].lower():
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
for i in range(len(s)):
    if s[i].lower() in "aeiouаоуыиэеёюя":
        vowels += 1
print("Гласныx:", vowels)
