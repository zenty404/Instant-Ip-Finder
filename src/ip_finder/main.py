#!/usr/bin/python3

from curses import window
import socket
from tkinter import *
import os
import sys
sys.path.append('__init__')
import get_ip as ad
import file_mg as file 
from art import *
from termcolor import colored
SEC_PATH = "/usr/bin/"


def find():
	ipAddress = socket.gethostbyname(url.get())
	result.delete(0, END)
	result.insert(0, ipAddress)

	

# ----------
# FENETRE :
# ----------

window = Tk()  # Création de a fenêtr 1e
window.geometry("300x200")
window.iconbitmap('ip-photo.png')
window.title("IP Finder")  # Titre de la calculatrice
window["bg"] = "#B2B4AC"  # Coleur de la fenêtre
window["relief"] = "raised"  # Profondeur de la fenêtre

# ----------
# crée la frame principale
# ----------
frame = Frame(window, bg='#B2B4AC')

# creer un titre
label_title = Label(frame, text="IP finder", font=("Helvetica", 20), bg='#B2B4AC', fg='black')
label_title.pack()

# creer un input
url = Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black')
url.pack()

# creer un bouton
find_button = Button(frame, text="Find !", font=("Helvetica", 20), fg='black', command=find)
find_button.pack(fill=X)

# creer le result
result = Entry(frame, font=("Helvetica", 20), bg='#B2B4AC', fg='black',)
result.pack()

# affciher la frame
frame.pack(expand=YES)


window.mainloop()  # Gestion de la fenêtre