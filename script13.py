from tkinter import *
import pyperclip
import random

root = Tk ()
root.geometry("700x300")


passwrd = StringVar()
passlen = IntVar()
passlen.set(12)

def generate():
    pass1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0', '', '!','@','#','$','%','^','&','*','(',')']
    password = ""
    for x in range(passlen.get()):
        password += random.choice(pass1)

    passwrd.set(password)
    

def copyclipboard():
    pyperclip.copy(random_password)

label(root, text="Password Generator",
