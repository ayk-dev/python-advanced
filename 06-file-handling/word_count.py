import re

with open('words.txt', 'r') as words_fh, open('input.txt', 'r') as text_fh:
    words = words_fh.read().split()
    text = text_fh.read()

words_occurrences = {}

for word in words:
    matches = re.findall(rf'[\s-]({word})[\s,.?!]', text, re.MULTILINE + re.IGNORECASE)
    words_occurrences[word.lower()] = len(matches)

with open('Even_lines/output.txt', 'w') as output_fh:
    for word, occurrences in sorted(words_occurrences.items(), key=lambda t: -t[1]):
        print(f"{word} - {occurrences}", file=output_fh)