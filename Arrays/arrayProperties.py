# Array Properties :-
# 1) typecode - It will return the datatype of the element in an array,
# 2) itemsize - It will return the size of single array element.

# Example :-

from array import *

#__main__

a=array("i",[20,40,60,80])
print("a =",a)

print("Type code =",a.typecode)
print("Item size =",a.itemsize , "bytes")

#end of __main__











