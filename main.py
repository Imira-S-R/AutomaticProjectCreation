# Automatic Project Creation Tool
# Made By Imira Randeniya

import os

# Getting the required Information
path_to_create = input('Enter path to create project: ')
projectName = input('Enter project name: ')
author = input('Enter author name: ')
fileExtension = input('Enter project file extension (ex- .py): ')

# Changing the directory
try:
    os.chdir(path_to_create)
except FileNotFoundError:
    print('[-] The File Location You Entered Is Not Valid')
    exit()

# Creating Required Directories & Files
print('[+] Creating Project Directory')
os.mkdir(projectName)
os.chdir(projectName)

print('[+] Creating file')
file = open(f'{projectName}{fileExtension}', 'w+')

# Adding a comment based on the file extension
if fileExtension == '.py':
    print('[+] Writing Information To The File')
    file.write(f'#Project Name: {projectName}\n')
    file.write(f'#Author: {author}\n')
elif fileExtension == '.dart' or fileExtension == '.java' or fileExtension == '.kt' or fileExtension == '.js':
    print('[+] Writing Information To The File')
    file.write(f'//Project Name: {projectName}\n')
    file.write(f'//Author: {author}\n')
elif fileExtension == '.html':
    print('[+] Writing Information To The File')
    file.write(f'<!--Project Name: {projectName}-->\n')
    file.write(f'<!--Author: {author}-->\n')
else:
    print('[+] Writing Information To The File')
    file.write(f'Project Name: {projectName}\n')
    file.write(f'Author: {author}\n')

print('[+] Successfully Created The Files')
print('[+] Done.')

file.close()


