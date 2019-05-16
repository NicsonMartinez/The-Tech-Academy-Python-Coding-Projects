# The Tech Academy - GUI Drill 3
#
# Drill Description: 
# In this drill I will be creating a gui that cut an pastes .txt files found from one directory to another
# selected directoy. Please read the README.txt file for a detailed Drill Description.
#
# Nicson Martinez
# 5/15/19

import os
from tkinter import * 
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime

class TheMainWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(605, 260)) # (width,height)
        self.master.title('Check Files')
        self.master.config(bg='lightgray')
        
#-------------------------------------GUI Row 0-------------------------------------------

        self.btnBrowse1 = Button(self.master, text='Browse...', width=15, height=2, command = self.browseDirectory)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(50,0))

        self.txtBox1 = Entry(self.master, font=('Arial', 10), fg='black', width=58)
        self.txtBox1.grid(row=0, column=1, padx=(30,0), pady=(50,0))

#-------------------------------------GUI Row 1-------------------------------------------

        self.lblMsg = Label(self.master, text='Log:', font=('Arial', 10), fg='black', width=10, bg='lightblue')
        self.lblMsg.grid(row=1, column=0, padx=(25,0), pady=(5,0))

        self.lblMsg1 = Label(self.master, text='', font=('Arial', 10), fg='black', width=55, bg='lightgray')
        self.lblMsg1.grid(row=1, column=1, padx=(5,0), pady=(0,0))

#-------------------------------------GUI Row 2-------------------------------------------

        self.lblMsg2 = Label(self.master, text='', font=('Arial', 10), fg='black', width=55, bg='lightgray')
        self.lblMsg2.grid(row=2, column=1, padx=(5,0), pady=(0,20))

#-------------------------------------GUI Row 3-------------------------------------------

        self.btnBrowse2 = Button(self.master, text='Cut & Paste Here', width=15, height=2)
        self.btnBrowse2.grid(row=3, column=0, padx=(20,0), pady=(0,0))

        self.txtBox2 = Entry(self.master, font=('Arial', 10), fg='black', width=58)
        self.txtBox2.grid(row=3, column=1, padx=(30,0), pady=(0,0))

#-------------------------------------GUI Row 4-------------------------------------------

        self.btnCloseProg = Button(self.master, text='Close Program', width=15, height=2, command=self.close)
        self.btnCloseProg.grid(row=4, column=1, sticky=SE)

#---------------------------------[ Button Functions ]--------------------------------------

    def browseDirectory(self):
        # This is done in case the user decided to type something in the textbox before
        # pressing the [Browse...] button.
        test = self.txtBox1.get() 
        print("Below is the text the user wrote on textbox 1 before clicking on the Browse button: \n'{}'\n".format(test))

        test1 = self.txtBox1.delete(0, END) #Deletes chars located in index 0,1,2,3...until END.
        print("The text, '{}' has now been deleted for data normalization: \n{}\n".format(test,test1))
        
        dirVariable = filedialog.askdirectory()
        self.lblMsg1.config(bg='lightblue', text='We are now locating the .txt files in the directory selected!')
        self.txtBox1.insert(0, dirVariable)
        fPath = self.txtBox1.get()
        print('This is the directory that was selected: \n{}\n'.format(fPath))

        directoryList = os.listdir(fPath) #Creates list of files in a specific directory.
        print("All files in directory, {} are listed below: \n{}\n".format(fPath,directoryList))
        
        print("The text files detected are: ")
        count = 0
        for file in directoryList:
            if file.endswith('.txt'):
                abPath = os.path.join(fPath, file) #Concatinates the path directory with a txt file found through each iteration. 
                fModTime = os.path.getmtime(abPath) #Gets last modified time.
                formattedTime = datetime.fromtimestamp(fModTime).strftime('%m-%d-%Y %H:%M:%S') #Formats the time in a way that humans can understand
                count += 1 #Increments count by 1 through each iteration.
                print("File {}. {} : Last-Modified Time {}".format(count,abPath,formattedTime))


    def close(self):
        self.master.destroy()

if __name__=="__main__":
    root = Tk()
    App = TheMainWindow(root)
    root.mainloop()
