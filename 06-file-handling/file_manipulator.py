import os

while True:
    command = input()
    if command == 'End':
        break

    cmd, *others = command.split('-')
    if cmd == 'Create':
        file_name = others[0]
        with open(file_name, 'w') as file_fh:
            pass

    elif cmd == 'Add':
        file_name, content = others
        try:
            file_fh = open(file_name, 'a')
        except FileNotFoundError:
            file_fh = open(file_name, 'w')
        finally:
            file_fh.write(content+'\n')
            file_fh.close()

    elif cmd == 'Replace':
        file_name, old_string, new_string = others
        try:
            file_fh = open(file_name, 'r')
            new_file_lines = []
            for line in file_fh:
                if old_string in line:
                    new_line = line.replace(old_string, new_string)
                else:
                    new_line = line
                new_file_lines.append(new_line)
            with open(file_name, 'w') as new_file:
                new_file.write(''.join(new_file_lines))

        except FileNotFoundError:
            print('An error occurred')
        finally:
            file_fh.close()

    elif cmd == 'Delete':
        file_name = others[0]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')



