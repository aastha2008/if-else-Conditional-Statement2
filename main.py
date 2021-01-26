'''
01/25/2021

Homework


#Homework_Data types

name=input("Enter your name: ")
age=input("Enter your age: ")
drink=input("Enter your favorite drink: ")
grade=input("Enter your grade: ")

print ("I am " + name + ". \nMy age is " + age + ". \nI love to drink " + drink + ". \nMy favorite grade is " + grade + ".")

Review - Opearators:
 1. Math Operators. (Arithmetic Operators)
  addition, +
  substraction, -
  multiplication, *
  division, /  (Exact answer)
  division, // (Quotient)
  modulo, %. (Remainder)
  exponent, **



5/2 = 2.5
5 // 2 = 2
5%2=1
9%10=9
8 % 2 = 0

 2. Assignment Operators
 = (assignement)
 += (Addition Assignment)
-= (Subtract Assignment)
*=
/=
//=
%=
**=

Rule:
A variable must be declared before using assignment Opearators

a +=4 ## a = a + 4. (what is a??). Need to define a before

 3. Comparison Operators
 == (equal to)
!= (not equal to)
< (less than)
<= (less than or equal to)
> (greater than)
>= (greater than or eqaul to)

5 == 4 (False)
6 >= 7 (False)
0 != "zero"  (True)
0 != "0" (True)

if/else conditional statement:

if (CONDITION):
  BODY
else:
  BODY

'''
print(5/2)
print(5//2)
print(5%2)
print(9%10)
print(8%2)

a=1
a += 4. # a = a + 4
print(a)

print(6 >= 7)
print (0 != int("0"))
print (0 == int("0"))

a = 21
if (a % 3 != 0):     # 21 %3 = 0
 print ("Hi")
else:
  print ("Bye")


  z = 16

  if (z % 3 == 0):   # 16 % 3 = 1
    print ("I will go to bed early")
  
  if (z % 5 == 0):  # 16 % 5 = 1
    print ("I love python")