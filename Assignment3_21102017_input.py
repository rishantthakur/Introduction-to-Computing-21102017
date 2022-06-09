#Q1

a=int(input("Enter your number: "))
b=bin(a)
print(b[2:]) 


#Q2
b = float(input('Enter first number: '))
a = input('Enter sign(+, -, *, / or q for quit): ')

while (a!='q'):
    if a=='+':
        b = b + float(input('Next number: '))
    elif a == '-':
        b = b - float(input('Next number: '))
    elif a == '*':
        b = b * float(input('Next number: '))
    elif a == '/':
        b = b / float(input('Next number: '))
    else:
        print('Invalid operator, try again')
    a = input('Enter next sign(+, -, *, / or q for quit): ')

print(b)


#Q3
import math

n = 10
r = 10
α = 10
β = 10
y2 = 20
y1 = 10
x2 = 30
x1 = 10

exp1 = (3+4) * (5)
exp2 = ((n)*(n-1)) / 2
exp3 = 4*(math.pi) * (math.pow(r,2))
exp4 = math.sqrt(r*(math.pow(math.cos(α), 2)) + r*(math.pow(math.sin(β), 2)))
exp5 = (y2 - y1)/(x2 - x1)

print(exp1)
print(exp2)
print(exp3)
print(exp4)
print(exp5)


#Q4
for i in range(5):
    print(i, end=" ")
print()

for i in range(3,10):
    print(i, end=" ")
print()

for i in range(4,13,3):
    print(i, end=" ")
print()

for i in range(15,5,-2):
    print(i, end=" ")
print()

for i in range(5,3):
    print(i, end=" ")

    
#Q5
No_H = int(input('Enter number of Hydrogen Atoms: '))
No_C = int(input('Enter number of Carbon Atoms: '))
No_O = int(input('Enter number of Oxygen Atoms: '))

print('Molecular weight of compound is:', (No_H * 1.00794) + (No_C * 12.0107) + (No_O * 15.9994), 'grams/mole')


