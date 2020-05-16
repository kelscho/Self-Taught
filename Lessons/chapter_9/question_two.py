"""Write a program that asks a user a question, and saves their answer to a file."""


import os

path=r"C:\Users\Kelly\AppData\Local\Programs\Python\Python38-32\Lessons\chapter_9"
# file object is named 'f' in this case (must be inside the with statement)
ls=input("What is your name? ")
with open("ls.txt","w")as f:
    f.write(ls)

