""" 
8. Write a python program to delete the set completely.
 """
s1=input("Enter the elements with coma:")
s2={e for e in s1.split(",")}
print(s2)
del s2
print(s2)
#================================================OUTPUT=================================#
# {'"Nitro-5"', '"Hp"', '2000', '"Acer"', '90.78'}
#After delete the set:
# NameError: name 's2' is not defined. Did you mean: 's1'?
