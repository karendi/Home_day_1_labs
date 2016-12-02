#define a class Animal 
#the type of animal is either domestic
class Animal(object):
    def __init__(self , name ,type, no_of_legs , fur = False ):
        self.name = name
        self.no_of_legs = no_of_legs
        self.fur = fur

    def animal_eats(self , food):
        name = self.name
        return (name,"eats" , food)

    #example of encapsulation, with use of private methods.prevents data from being edited
    def __alive(self , alive):
        alive = True
        return alive




#the subclass Pet inherits from Animal class
class Pet(Animal):
    def __init__(self , gender):
        Animal.__init__(self , name , 'domestic' , no_of_legs, True)
        self.gender = gender

#custom methods for the subclass Pet
    def get_number_of_legs(self):
        return self.no_of_legs

    def get_gender(self):
        name = self.name
        return(name , "is a" , gender)
