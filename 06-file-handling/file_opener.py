try:
    open('Even_lines/text.txt')
    print('File exists')
except FileNotFoundError:
    print('File not found')

# Second option - better option

import os.path

print('File exists' if os.path.exists("Even_lines/text.txt") else 'File not found')
