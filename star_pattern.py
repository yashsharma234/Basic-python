n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    print("*"*(i),end="\n")
    print(" "*(i-1),end=" ")
for j in range(n,-1):
   print("*"*(j-1),end=" ")  

   print(" "*(j-1),end=" ")  

