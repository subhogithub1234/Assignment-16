""" 
10. Write a python program to find the maximum and minimum value in a set.
 """
s1=input("Enter the elements with coma:")
s2={e for e in s1.split(",")}
print(s2)
print("maximum value in s2 set is:",max(tuple(s2)),"minimum value is s2 set is:",min(tuple(s2)))