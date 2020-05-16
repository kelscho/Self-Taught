"""Take the items in this list of lists:[["Top Gun","Risky Business",
"Minority Report"],["Titanic","The Revenant","Inception"],{"Training Day",
"Man on Fire","Flight"]] and write them to a CSV file. The data from
each list should be a row in the file, with each item in the list seperated
by a comma."""


import os
import csv

path=r"C:\Users\Kelly\AppData\Local\Programs\Python\Python38-32\Lessons\chapter_9"
#file object is named 'csvfile' in this case (must be inside the with statement)
movies=[["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]                                                                                          
with open("movies.csv","w") as csvfile:
    spamwriter=csv.writer(csvfile,delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
