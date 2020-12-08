import os

# file = open('asd.txt', 'r')
#
# print(file.read(5))
#
# print(file.readline(5))
#
# print(file.readlines())
# file.close()

###########################################

# file = open('loremipsum.txt', 'r')
#
# for line in file:
#     print(line, end='')
# file.close()

###########################################

file = open('python.txt', 'w')
file.write('This the write command\n')
file.write('It allows us to write in a particular file\n')
file.close()

file = open('python2.txt', 'a')
lines = ['We ', 'put ', 'more ', 'text ', 'here.']
file.writelines(lines)
file.close()

# os.remove('python.txt')
# os.remove('python2.txt')
