# Array :- An array is a group of element of SAME data types.

# Syntax :-  1) from array import *
# #             arr_obj_name=array(data-type_code,[val1,val2,...])

'''

# Example-1 :-

from array import *
# __main__

a=array("i" , [89,74,92])
print("a =",a)
#end of __main__



# Accessing Array Element :-

# Example :-

from array import *
# __main__
a=array("d",[25.56,89.60,12.34])
print("Array = ",a)

print("Forward Indexes : ")
print("a[0] = ",a[0])
print("a[1] = ",a[1])
print("a[2] = ",a[2])

print("Reverse Indexes : ")
print("a[-1] = ",a[-1])
print("a[-2] = ",a[-2])
print("a[-3] = ",a[-3])


# 2) Immutable Iterable :- we can add new element and delete existing element.
#for example :- Tuple , String ,Frozenset

# 1) Mutable Iterable :- we can add new element and delete existing element.
#for example :-  Array , List , Set , Dictionary .

# Example :-

from array import *
# __main__
a=array("i",[29,56,34,13])
print("a =",a)
a[1]=89
print("a after adding new element = ",a)
del a[3]
print("a after delete an element = ",a)
a.append(75)
print("a after append an element = ",a)

#end of __main__




# Example :- WAP to display all the elements in array.

from array import *
# __main__

a=array("i" , [67,90,59,35])

for i in range(0,len(a)):
    print(a[i])

'''

# Example :- WAP to display all the elements in array by using for-in loop.

from array import *
# __main__

a=array("d",[1.2,5.4,8.2,3.9])

for x in a:
    print(" array element =", x)







