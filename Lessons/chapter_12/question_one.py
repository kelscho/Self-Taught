"""Define a class called Apple with four instance variables that represent
four attributes of an apple."""
class Apple():
    
    def _init_(self,length,weight,color,price):
        self.length=length
        self.weight=weight
        self.color=color
        self.price=price
    def print_attr(self):
        print("The apple has a length of {} inches and it has a weight of about {} pounds, it is {} in color and costs {} cents per pound.".format(self.length,self.weight,self.color,self.price))
    length=4
    weight=.2
    color="red"
    price=.25
apple=Apple()
apple.print_attr()
