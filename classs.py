class learn:

    def __init__(self,radius=1):
        self.radius = radius
        self.area=radius*radius*3.14
        # self.circum = 2*3.14*radius

        # pass
    
    def reset_area(self,new_radius):
        self.radius= new_radius
        self.area = new_radius*new_radius*3.14
        

        # return nm/
    def circumference(self):
        r=self.radius
        self.cir= r+1
        return self.cir

l=learn()
# l.circumference()
print(l.circumference())
# l.reset_area(4)
# print(l.area)
class  calculator:
    

    def __init__(self,a=1,b=5):
        self.num1= a
        self.num2 = b
    

    def addition(self):
        return self.num1 + self.num2


    def substraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
        


y = calculator()

print( 'additon is :' ,y.addition() )

        


    



