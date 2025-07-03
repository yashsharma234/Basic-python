# list methods which gives alter list 
l1=[1,2,3,4,5,6,7,89,23,35,30]

l1.sort()#sort the int 
print(l1)

l1=["yash","dhruve","karan","vikash","vivek","tanishk","raj","krsih","yuvansh"]
l1.sort()

print(l1)#sort the string
l1=[1,2,3,4,5,6,7,89,23,35,30,"yash","dhruve","karan","vikash","vivek","tanishk","raj","krsih","yuvansh"]
print(l1)


####################################
l1=[1,2,3,4,5,6,7,8,9]
print(l1.pop(2))#pop the element of index 2
l1.pop()
print(l1)#pop randomly element

######################################################

l1=[1,2,3,4,5,6,7,8,9]
l1.reverse()#reverse method
print(l1)

##############################################
l1=[1,3,4,5,6,78,8,9,23,34,"yash"]
l1.remove(78)#remove particular element
print(l1)

#################################
l1=[1,2,3,4,5,6,7,8,9,10]
l1.append(23)

#######################################
new_list = l1 + [7, 8, 9]#add list into list
print(new_list)


##############################
index = l1.index(4)  # Get the index of the first occurrence of 4
print(index)

########################################3
count = l1.count(2)  # Count the number of occurrences of 2
print(count)


l=[1,22,23,35,72]
print(sum(l))