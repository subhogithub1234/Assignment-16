""" 
1. Write a python program to store all the programming languages known to you using
Set.

 """
# Solution 1:

x=int(input("How many element you want to be enter:"))
s1=set()
print("Enter the elements:")
for e in range(x):
    e=input()
    s1.add(e)

print(s1)   

#Solution 2:

s=input("Enter elements separated by Cama:")

s1={eval(e) for e in s.split(',')}
print(s1)
#---------------------------------------OUTPUT-------------------------------#
{'C', 'Python', 'Java', 'C++'}
