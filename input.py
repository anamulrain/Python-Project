# to take input from user we can do as
a = input()
print(a)

# so here input is a function where we can give what input we want to give like a string or number or anything we want
# similar example

x = input("Enter your name: ")
print("My name is ", x) 

''' in this example x in a input variable where a user can input their name or any
thing that they want to and then print function will 
print the result that we want to'''



#  In the given example below the result we expecting will be sum of the number but it gives the string by cancanating 
c = input("Enter your first number: ")
d = input("Enter your second number: ")
print(c + d)

''' so to not get this type of error we have to give the proper 
datatype because the python convert the given value into string if 
we didin'tgive the proper datatype so for that we know about type cast.
'''
# so to get the value in number we can use casting

print( int(c) + int(d))
'''
here the string value of c and d will convert into integer valu
'''

# exercise for the input using castng


y = input("Enter your first number: ")
z = input("Enter your second number: ")
print(y + z)
print(int(y) + int(z))
print(float(y) + float(z))


