from tkinter import *
import tkinter.messagebox
import datetime
import os
import subprocess
import threading
import time

class MainWindow:

    def buttonListener1(self,event):
        if self.button1['text'] == 'adb logcat':

            print("connecting to the device...")
            subprocess.call("adb wait-for-device")

            self.button1['text']='stop logcat'
        else:
            self.button1['text'] = 'adb logcat'


    def buttonListener2(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 2 dialog")
    def buttonListener3(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 3 dialog")
    def buttonListener4(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 4 dialog")

    def  __init__(self):
        self.frame = Tk()

        self.button1 = Button(self.frame,text = "adb logcat",width = 10,height = 5)
        self.button2 = Button(self.frame,text = "button2",width = 10,height = 5)
        self.button3 = Button(self.frame,text = "button3",width = 10,height = 5)
        self.button4 = Button(self.frame,text = "button4",width = 10,height = 5)

        self.button1.grid(row = 0,column = 0,padx = 5,pady = 5)
        self.button2.grid(row = 0,column = 1,padx = 5,pady = 5)
        self.button3.grid(row = 1,column = 0,padx = 5,pady = 5)
        self.button4.grid(row = 1,column = 1,padx = 5,pady = 5)

        self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
        self.button4.bind("<ButtonRelease-1>",self.buttonListener4)

        self.frame.mainloop()

window = MainWindow()