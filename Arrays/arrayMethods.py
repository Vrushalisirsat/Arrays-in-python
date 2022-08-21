# Array Methods :-

# 1) arr_obj.append(value) - It will add the given value in the end of array.

'''

# Example -

from array import *

#__main__

a=array("i",[12,46,74,87])
print("a =",a)
a.append(30)
print("Array after append the new element :",a)



# 2) arr_obj.count(value) - It will count the number of occurances of the given value and return it.

# Example -

from array import *

#__main__

a=array("i" , [10,20,30,40,20])
print("a =",a)

print('count =',a.count(20))

#end of __main__


# 3) arr_obj.extend(arr_obj/tuple_obj/list_obj/set/dictionary) :- It will add all the elements from the given iterables in the end of array.

# Example -

from array import *
#__main__

a=array("i" , [10,20,30,40])
print("a =",a)


t=(78,98)                 # tuple
l=[30,80]                 #list
d={97:"a" , 98:"b"}        #dictionary
s={60,40}                #set
y=array("i",[999,101])

a.extend(t)
a.extend(l)
a.extend(d)
a.extend(s)
a.extend(y)

print("a = ",a)
#end of __main__


# 3) arr_obj.formlist(list_obj) :- It will add all the elements from the given list object at the end of array.

# Example -

from array import *
#__main__

a=array("i" , [10,20,30,40])
print("a =",a)

x=[99,77,55]
a.fromlist(x)
print("a =",a)
#end of __main__


'''

# 3) list_obj=arr_obj.tolist() :- It will return all the element from array in list

# Example -

from array import *
#__main__

a=array("i" , [10,20,30,40])
x=a.tolist()

print("x =",x)
print("Data type of x =",type(x))

