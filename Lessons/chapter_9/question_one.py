"""Find a file on your computer and print it's contents using Python."""


import os

path=r"C:\Users\Kelly\AppData\Local\Programs\Python\Python38-32\Lessons\chapter_9"
#Print it's contents
with open("Chi.rtf","r")as f:
    print(f.read())
