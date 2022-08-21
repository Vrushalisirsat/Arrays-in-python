# Finding Length of an array :- length of an array can be found by using 2 function
# 1) arr_obj.__len__()        ,    2) len(arr_obj)


# Example :-

from array import *
# __main__
a=array("i",[10,20,30,40,50])
print("a = ",a)
print("Length of array : ",len(a))

x = a.__len__()
print("length of array : ",x)
