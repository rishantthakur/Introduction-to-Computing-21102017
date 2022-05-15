# Assignment 2.


# Question 1.
'''Performing operations on strings.'''

print("\nString Operations\n")

string = "Python is a case sensitive language"

print("The original Sting is: \"{}\"".format(string))

    # Part a.

# Finding the length using length function.
length = len(string)

print("\tlength of the given string:",length)

    # Part b.

# Reverseing the order using string slicing.
print("\tString in reversed order is: \"{}\"".format(string[::-1]))

    # Part c.

# Slicing and storing in a new variable new_string.
new_string = string[10:26]

print("\tNew String: \"{}\"".format(new_string))

    # Part d.

# Replacing words in using replace command.
print("\tString after the changes: \"{}\"".format(string.replace("a case sensitive", "object oriented")))

    # Print e.

# Finding index of 'a' using .find.
print("\tIndex of \"a\" in the given string:",string.find("a"))

    # Part f.

# Removing the white spaces using .replace.
print("\tString after removing the white spaces: \"{}\"".format(string.replace(" ", "")))

print("-" * 80)

# Question 2.
'''Program to do String Formatting.'''

print("\nString Formatting\n")

name = input("Enter your Name:")
sid = int(input("Enter your SID:"))
dept_name = input("Enter the name of your department:")
cgpa = float(input("Enter your CGPA:"))

print()

# String formatting using .format() command.
print("Hey {0} Here!\
    \nMy SID is {1}\
    \nI am from {2} department and my CGPA is {3}.".format(name, sid, dept_name, cgpa))

print("-" * 80)

# Question 3.
'''Program to use Bitwise Operators.'''

print("\nBitwise Operators\n")

a = 56
b = 10

print("a:", a)
print("b:", b)

print()

    # part a.
    # AND operator.

print("a & b:", a & b)

    # part b.
    # OR operator.

print("a | b:", a | b)

    # part c.
    # XOR operator.

print("a ^ b:", a ^ b)

    # part d.
    # left bit shifting.

print("Left shifting both a and b by 2 bits: a-{0},b-{1}".format(a << 2, b << 2))

    # print e.
    # right bit shifting.

print("Right shifting a by 2 and b with 4 bits: a-{0},b-{1}".format(a >> 2, b >> 4))

print("-" * 80)



# Question 4.
'''Program to compare Strings.'''

print("\nString Comparison\n")

user_input = input("Enter the String:")

# condition to check if "name" present in user_input.
if "name" in user_input:
    print("Yes")

# condition to check if "name" is not present in user_input.
else:
    print("No")



# Question 5.
'''Program to Check Validity of a Triangle.'''

print("\nTriangle Validity Checker\n")

side1 = input("Enter the Length of first side:")
side2 = input("Enter the Length of second side:")
side3 = input("Enter the Length of third side:")

# Converting to int datatype.
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

# condition to check if any of the three lengths is greater than the sum of other two.
if (side3 >= side1 + side2) or (side2 >= side1 + side3) or (side1 >= side2 + side3):
    print("No, Triangle Cannot be formed.")

else:
    print("Yes,Triangle Can Be formed.")



#Question 6.
    '''Program to count number of bits needed to be flipped to convert 'a' to 'b'.'''
    
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))

num=a^b
count=0
while (num!=0):
  num=num&(num-1)
  count +=1

print("Number of bits needed to be flipped to convert a to b is:",count)


