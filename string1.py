# String 
'''
Any thing written in single or double quotes can be considered as a string.
'''
# Example
name = "Anamul"  #double quotes string example
print("My name is ", name)

friendName = 'Rahul' #single quotes string example
print("My Friend name is",friendName )

bio = '''Hello, I am MD Anamul Rain.     
I am an undergraduate and recently seeking for a job for full-stack developer.
And also i am learning python myself''' # multi line string, 
print("BIO\n",bio)

# Accessing Character of the string
'''
In python, string is like array and we can access the character of the string using its index number starting from 0.
And to access the character we have to use [] and inside the square bracket we have to define the index and also we
can access the character from where we want as well.
'''
# Example
print(name[2]) #we have a name veriable above and here we can access its character
print(name[5]) 

# Looping in the character of string
'''
We can also use the for loop in the string character to use every single letter
'''
# Example
for character in name:
    print(character)

# String slicing and Operations of string
'''
1. length of string
we can find the length of string using len() function
'''
#  Example
fruit = "Mango"
lenFruit = len(fruit)
print("Mango is a", lenFruit, "letter of word.")

'''
2. String as an array
A string is essentially a sequence of characters also called as an array.
And we can acess the element of character of this array
'''
# Example
names = "Rahul, Sahim"
print(len(names))
print(names[0:5])# semicolon is used to declear the starting and ending point and the last number we enter will always be n-1 i.e 5-1 = 4 we have to remember this in mind
print(names[3:9])

print(names[:]) # if we will not define starting and ending point then pythin automatically place the start point that is 0 and the end point len().
print(names[:7]) 
print(names[4:])

print(names[0:-4]) #while in negative index, where we give the negative numnber the python automatically subtract that from the total length of the variable i.e len(names)-4.
print(names[-8:-2])

nm = "Harry"
print(nm[-4:-2])

# String methods
'''
Python has a set of built-in methods that you can use on strings. 
capitalize()	        Converts the first character to upper case
casefold()	            Converts string into lower case
center()	            Returns a centered string
count()	                Returns the number of times a specified value occurs in a string
encode()	            Returns an encoded version of the string
endswith()	            Returns true if the string ends with the specified value
expandtabs()	        Sets the tab size of the string
find()	                Searches the string for a specified value and returns the position of where it was found
format()	            Formats specified values in a string
format_map()	        Formats specified values in a string
index()	                Searches the string for a specified value and returns the position of where it was found
isalnum()	            Returns True if all characters in the string are alphanumeric
isalpha()	            Returns True if all characters in the string are in the alphabet
isascii()	            Returns True if all characters in the string are ascii characters
isdecimal()	            Returns True if all characters in the string are decimals
isdigit()	            Returns True if all characters in the string are digits
isidentifier()	        Returns True if the string is an identifier
islower()	            Returns True if all characters in the string are lower case
isnumeric()	            Returns True if all characters in the string are numeric
isprintable()	        Returns True if all characters in the string are printable
isspace()	            Returns True if all characters in the string are whitespaces
istitle()	            Returns True if the string follows the rules of a title
isupper()	            Returns True if all characters in the string are upper case
join()	                Joins the elements of an iterable to the end of the string
ljust()	                Returns a left justified version of the string
lower()	                Converts a string into lower case
lstrip()	            Returns a left trim version of the string
maketrans()	            Returns a translation table to be used in translations
partition()	            Returns a tuple where the string is parted into three parts
replace()	            Returns a string where a specified value is replaced with a specified value
rfind()	                Searches the string for a specified value and returns the last position of where it was found
rindex()	            Searches the string for a specified value and returns the last position of where it was found
rjust()	                Returns a right justified version of the string
rpartition()	        Returns a tuple where the string is parted into three parts
rsplit()	            Splits the string at the specified separator, and returns a list
rstrip()	            Returns a right trim version of the string
split()	                Splits the string at the specified separator, and returns a list
splitlines()	        Splits the string at line breaks and returns a list
startswith()	        Returns true if the string starts with the specified value
strip()	                Returns a trimmed version of the string
swapcase()	            Swaps cases, lower case becomes upper case and vice versa
title()	                Converts the first character of each word to upper case
translate()	            Returns a translated string
upper()	                Converts a string into upper case
zfill()	                Fills the string with a specified number of 0 values at the beginning
'''