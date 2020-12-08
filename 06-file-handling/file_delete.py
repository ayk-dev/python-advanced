import os

try:
    os.remove('my_first_file.txt')
    print('File deleted successfully')
except FileNotFoundError:
    print('File already deleted')
finally:
    print('Program closed')