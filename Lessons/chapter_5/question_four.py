"""Write a program that lets the user ask your height, favorite color, or
favorite author and returns the result from the dictionary you created in the
previous challenge."""
me={"5ft9in":"correct","blue":"correct","Crighton":"correct"}
u=input("What is my height, my favorite color or my favorite author?")
if u in me:
    guess=me[u]
    print(guess)
else:
 print("Nope, try again")
