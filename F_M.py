#!/usr/bin/env python
# coding: utf-8

# In[100]:


import shutil
import os
import Path
import pandas as pd

Path.createDirPath()

class FileManager:
    
    def commands(self):
        d1={'CUR':'currentDir','CF':'createFolder','DF':'deleteFolder','CD':'changeDir','MF':'makeFile','WF':'writeFile','RF':'readFile','DFI':'delFile','CP':'copyFile','MFI':'moveFile','REF':'renameFile'}
        d1_pd=pd.Series(d1)
        commands = pd.DataFrame({'Названия команд': d1_pd})
        print(commands)
    
    def currentDir(self):
        print(os.getcwd())
    
    def createFolder(self, name):
        os.mkdir(name)
        
    def deleteFolder(self, name):
        os.rmdir(name)
        
    def makeFile(self, file_name):
        file = open(file_name, "w+")
        file.close()
        
    def writeFile(self, file_name, w):
        try:
            file = open(file_name, "a")
            file.write(w)
            file.close()
        except FileExistsError:
            print('Такого файла не существует')
            
    def readFile(self, file_name):
        try:
            file = open(file_name, "r")
            print(file.read())
            file.close()
        except FileExistsError:
            print('Такого файла не существует')
            
    def delFile(self, file_name):
        try:
            os.remove(file_name)
        except FileExistsError:
            print('Такого файла не существует')
            
    def copyFile(self, file_name, new_file_name):
        try:
            shutil.copy(file_name, new_file_name)
        except FileExistsError:
            print('Такого файла не существует')
            
    def moveFile(self, file_name, new_path):
        try:
            shutil.move(file_name, new_path)
        except FileExistsError:
            print('Такого файла не существует')
            
    def renameFile(self, file_name, new_file_name):
        try:
            os.rename(file_name, new_file_name)
        except FileExistsError:
            print('Такого файла не существует')
        
    def changeDir(self, path):
        try:
            if path=='up':
                if os.getcwd()=='C:\\Users\\dsstk\\Documents\\Python\\file':
                    print('Ошибка! Выход за предел рабочей папки')
                else:
                    os.chdir('..')
            else:
                if os.path.exists(os.getcwd()+'\\'+path):
                    os.chdir(os.getcwd()+'\\'+path)
                else:
                    os.mkdir(os.getcwd()+'\\'+path)
                    os.chdir(os.getcwd()+'\\'+path)
        except FileNotFoundError:
            print('Файла не существует')


# In[ ]:




