class A:

    def __init__(self):
        self.name1 = 'name1'


class B:

    def __init__(self):
        self.name2 = 'name2'

    
        
class D(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def prin(self):
        print(self.name2,self.name1)


class C:


    def __init__(self,name):
        self.name = name


    def see(self):
        print( 'name is ', self.name)   

class D(C):

    def __init__(self , name,age):
        C.__init__(self,name)
        self.age = age
    

    def get(self):
        return self.name , self.age


ob = D('nisha',56)
print(ob.get())





     
