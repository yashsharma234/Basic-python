
#write a  program to create a dictinary of hindi words with values as their english meaning translation . provide user with an option to look up!

words={
    "madad":"help",
    "kursi": "chair",
    "billi":"cat"   }
print(words["madad"])
word=str(input("enter the word you want meaning of: "))
print(words[word])


#write a program to input eight numbers from the user and display all the unique number(once)
s=set()
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
d=(input('enter the number'))
s.add(int(d))
print(s)

#print differnet s
s=set()
s.add(18)
s.add("18")
s.add(18.4)
print(s)

#write the name of key and values pf the friend input

s={}
name=input("enter the value: ")
lan=input("enter the key: ")
s.update({name:lan})
print(s)

