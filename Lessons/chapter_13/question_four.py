"""Create a class called Horse and a class called Rider. Use composition
 to model a horse that has a rider."""
class Horse():
    def __init__(self, name):
        self.name = name
        
        
class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

     
the_horse = Horse('Trigger')
the_rider = Rider('Lone Ranger', the_horse)  
print(the_rider.horse.name)    

    