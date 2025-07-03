

a1 = int(input("Enter the value of a1: "))   
a2 = int(input("Enter the value of a2: "))   
a3 = int(input("Enter the value of a3: "))   
a4 = int(input("Enter the value of a4: "))   

greatest = max(a1, a2, a3, a4)
print("The greatest number is:", greatest)

name=str(input("enter the name"))
if("harry".lower() in name.lower()):
    print("it talk about the haarry")
else:
    print("its  not talk about the harry")    


n=int(input("enter the value of n:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


l=["yash","raj","vivek","vikash","karan","keshav","aakash","yuvansh"]
for name in l:
    if(name.startswith("v")):
        print(f"hello {name}")    
#program for prime no
j=int(input("enter the value of j:"))
for j in range(2,n):
    if(n%2)==0:
        print("no is not prime number")
else:
    print("no is prime")        

#program for print sum of no
n=int(input("enter the number:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)    

#write a prgram to amke adifference in incraseing order like 1,2,3,4,5
n=int(input("enter the number:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
    print(sum)
#write a factorial program
n=int(input("enter the value of n:"))
product=1
for i in range(1,n+1):
    product=product*i
print(product)    