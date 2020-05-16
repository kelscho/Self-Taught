"""Write a function that converts a string to a float and returns the result.
Use exception handling to catch the exceptions that occur"""
def strum(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the String")
        
c=strum(40.5)  
print(c)

    
