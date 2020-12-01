vowels = ['a', 'o', 'u', 'e', 'i']

text_without_vowels = ''.join(w for w in input() if w.lower() not in vowels)
print(text_without_vowels)