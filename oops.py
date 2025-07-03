class employee:  # isse class khete hai
    language="python"
    salary=3500000

    def __init__(self,name,salary,language):# dunder method
        self.name=name
        self.slary=salary
        self.language=language
        print("here i am creatong a dunder method")

    def getinfo(self):#isme self likhna jaroroi hai
        print(f"the language is {self.language}.the salary is {self.salary}")



    # def greet(self):
    #     print("good morning")
    @staticmethod   #isme self ke koi jarrorat nahi hoti hai or object ka koi basta nahi hai
    def greet():
        print("good morning")


harry = employee("harry",350000,"javascript")
print(harry.name,harry.salary,harry.language)

harry.greet()
harry.getinfo()




#write a program to make a class of programmer in which data of empolyee is defined

class programmer():
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        print("the data of programmers is given below:-")

p=programmer("yash",2300000,203155)
print(p.name,p.salary,p.pin,p.company)      


#calculater function which gives the sqaue ,cube ,under root of the no
class calculator():
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the saquare  of this no is {self.n*self.n}")

    def cube(self):
        print(f"the cube root of this no is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the saquare root of this no is {(self.n)**1/2}")
            
p=calculator(4)
p.square()
p.cube()
p.squareroot()

class demo():

    b=4

o=demo()
print(o.b)#print karega 4 kyuke instance attributr absent hai

o.b=0#instance attribute present hai toh 0 he print karega 4 ke jagah


print(o.b)
print(demo.b)

    