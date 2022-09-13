""" 
5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
 """
thisset={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print("thisset=",thisset)
secondset.update(tuple(thisset))
print("secondset=",secondset)

#-----------------------------------------OUTPUT----------------------------------------
# thisset= {'Python', 'Java', 'SQL'}
# secondset= {'C', 'Python', 'Cpp', 'Java', 'NoSQL', 'SQL'}
