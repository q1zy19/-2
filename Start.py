#!/usr/bin/env python
# coding: utf-8

# In[72]:


import F_M as f

F = f.FileManager()

while True:
    command = input('Введите команду: ')
    command = command.split(' ')
    if command[0] == 'exit':
        break
        
    elif command[0] == 'commands':
        F.commands()
        
    elif command[0] == 'CUR':
        F.currentDir()

    elif command[0] == 'CF':
        F.createFolder(command[1])

    elif command[0] == 'DF':
        F.deleteFolder(command[1])

    elif command[0] == 'CD':
        F.changeDir(command[1])

    elif command[0] == 'MF':
        F.makeFile(command[1])

    elif command[0] == 'WF':
        contentWrap = input("Введите текст: ")
        F.writeFile(command[1], contentWrap)

    elif command[0] == 'RF':
        F.readFile(command[1])

    elif command[0] == 'DFI':
        F.delFile(command[1])

    elif command[0] == 'CP':
        F.copyFile(command[1], command[2])

    elif command[0] == 'MFI':
        F.moveFile(command[1], command[2])

    elif command[0] == 'REF':
        F.renameFile(command[1], command[2])

    else:
        print('Неверная команда!\n Для того чтобы увидеть полный список команд введите commands')

