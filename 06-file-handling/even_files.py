def reverse_order_of_words(line):
    reversed_words = line.split()[::-1]
    return ' '.join(reversed_words)


def replace_chars(line):
    chars_to_replace = ["-", ",", ".", "!", "?"]
    for ch in chars_to_replace:
        line = line.replace(ch, '@')
    return line


with open('text.txt', 'r') as text_fl:
    text_lines = text_fl.readlines()

result = []

for i in range(len(text_lines)):
    if i % 2 == 0:
        line = text_lines[i].strip('\n')
        line = reverse_order_of_words(line)
        line = replace_chars(line)
        result.append(line)

with open('output.txt', 'w') as output_fh:
    for line in result:
        print(line, file=output_fh)