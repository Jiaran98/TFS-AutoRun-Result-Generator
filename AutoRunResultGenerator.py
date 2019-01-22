#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import shutil
import re
import xlsxwriter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
# directory = os.fsencode("D:\TestAutomation\ReleasedScripts\Common")
# def CSdicGenerator(path, extension = ".cs"):
#     allCS = {}
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(extension) and file.startswith("TC_"):
#                 #print(os.path.join(root, file))
#                 allCS[file] = os.path.join(root, file)
#     return allCS


# In[5]:


def generateResult(trxFile, savePath, excelName):
    tree = ET.parse(trxFile)
    root = tree.getroot()
    fileName = root.get('id')
    tcId = {}
    for child in root[5]:
        tcId[child.get("testId")] = list(child)[0].get("testCaseId")

    entries = []
    i = 0
    errorList = {}
    messageList = {}
    testId = ""
    computerName = ""
    testName = ""
    StdOut = ""
    message = ""
    for child in root[6]:
        if child.get("outcome") == 'Failed':
            testId = tcId[child.get('testId')]
            computerName = child.get('computerName')
            testName = child.get('testName')
            InnerResults = list(child)
            for InnerResult in child.iter():
                if InnerResult.tag.endswith("StdOut"):
                    errorList[str(i)] = (InnerResult.text)
                    StdOut = (InnerResult.text)
                if InnerResult.tag.endswith("Message"):
                    messageList[str(i)] = (InnerResult.text)
                    message = (InnerResult.text)
                    i+=1
            entry = [testId, computerName, testName, message, StdOut]
            entries.append(entry)
    entries = np.array(entries)
    df = pd.DataFrame(entries, columns = ['TC_ID', 'ComputerName', 'TestName', "Error Message", 'StdOut'])
    writer = pd.ExcelWriter(savePath + '/' + excelName + '.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index = False, header = True)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    messagebox.showinfo("Done!", excelName + ".xlsx" + " has been generated!")


# In[6]:


def UploadFile(event=None):
    trx.set(filedialog.askopenfilename())
    filePath.configure(text=trx.get())
    print(trx.get())

def GetDirectory(event=None):
    directory.set(filedialog.askdirectory())
    savePath.configure(text=directory.get())
    print(directory.get())
    
def handle_click(a, b):
    if(a == '' or b == ''):
        print('lol')
    print(a)
    print(b)
    

window=Tk()
window.geometry("400x200")

trx = StringVar()
directory = StringVar()

upload = Button(window, text = 'Open', command = UploadFile)
upload.pack()

filePath = Label(window, text = '')
filePath.pack()

save = Button(window, text = 'Save', command = GetDirectory)
save.pack()

savePath = Label(window, text = '')
savePath.pack()

e = Entry(window)
e.pack()


run = Button(window, text = 'run', command = lambda: generateResult(trx.get(),directory.get(), e.get()))
run.pack()
window.mainloop()


# In[ ]:





# In[ ]:




