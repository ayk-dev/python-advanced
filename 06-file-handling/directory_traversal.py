import os
import pathlib

directory = input('Please enter exact directory location:\n')

files = {}

for file_name in os.listdir(directory):
    if '.' in file_name:
        name, extension = file_name.split('.')
        if extension not in files:
            files[extension] = []
        files[extension].append(name)

output_str = ''
sorted_files = dict(sorted(files.items(), key=lambda x: (x[0], x[1])))
for extension, names in sorted_files.items():
    output_str += f'.{extension}\n'
    for name in names:
        output_str += f'- - - {name}.{extension}\n'

print(output_str)

desktop_path = os.path.expanduser('~\\Desktop')
report_file_path = str(desktop_path) + os.path.sep + 'report.txt'

with open(report_file_path, 'w') as report_fh:
    report_fh.write(output_str)