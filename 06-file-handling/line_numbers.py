import string


def count_letters_and_punctuation(line):
    letters_count = 0
    punct_count = 0
    for ch in line:
        if ch in string.ascii_letters:
            letters_count += 1
        elif ch in string.punctuation:
            punct_count += 1
    return letters_count, punct_count


with open('text.txt', 'r') as text_fh:
    text_lines = text_fh.readlines()

with open('output.txt','w') as output_fh:
    for i in range(len(text_lines)):
        letter_count, punct_marks_count = count_letters_and_punctuation(text_lines[i])
        line_number = i + 1
        output_line = f'Line {line_number}: {text_lines[i].strip()} ({letter_count}) ({punct_marks_count})'
        print(output_line, file=output_fh)




