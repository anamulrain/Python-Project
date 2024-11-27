# Conditional operators
'''
Before grtting in it let's know about conditional operator first.
>, <, ==, <=, >=, !=
'''


# IF--elif statement
'''
Sometimes the programmer needs to check the evaluation of certain expression(s),
whether the exoressions evaluate to True or False. If the expression evaluate to False,
then the program execuation follows a different path than it would have if the expression 
evaluated to True. 

Based on this, the conditional statements are further classafied into following types:
1. if
2. if-else
3. if-else-elif
4. nested if-else-elif
'''
# Example of if
sub = input("Enter your subject ")
choice = "math", "science", "chemistry", "physics", "bio"

if (sub in choice):
    print("Your choice is write")


# Example of if-else
a = int(input("Enter your age: "))
print("Your age is ", a)

if(a>18):
    print("You can drive a car")
else:
    print("You are under 18 and can't drive a car")


# Example of if-elif-else
num = int(input("Enter your result "))

if(num >= 80):
    print("You are excelent student")
elif(num >= 60):
    print("You are a good student")
else:
    print("You are a average student")


# Example of nested if-elif-else
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Please enter a positive number.")
else:
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
        if age >= 16:
            print("You can pre-register to vote in some states.")
        else:
            print("You are not eligible to vote yet.")
    elif age < 65:
        print("You are an adult.")
        if age >= 18:
            print("You are eligible to vote.")
    else:
        print("You are a senior citizen.")
        if age >= 18:
            print("You are eligible to vote.")