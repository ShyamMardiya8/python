# student marks task in python

# marks = 60

marks = int(input("Enter Your Marks To Get Your Age"))

if(marks >= 90) :
    print("Grade: 'A'")
elif(marks >= 80 and marks < 90):
    print("Grade 'B'")
elif(marks >= 70 and marks < 80) :
    print("Grade C")
elif(marks >= 60 and marks < 70) :
    print("Grade D")


age = 90
if (age >= 18) :
     if (age >= 80) :
          print("your age is not allowed to drive")
     else:
        print("can drive")
else :
     print("your age less than 18")



# create one odd and even program in python

number = int(input("enter your number and check number is odd or even :"))

if(number % 2 == 0) : 
     print("your number is even")
else :
     print("your number is odd")


# find the number of user entered greater than 

numberOne = int(input("enter a first number"))
numberTwo = int(input("enter your second number"))
numberThree = int(input("enter yout third and last number"))

if(numberOne >= numberTwo and numberOne >= numberThree) :
    print("biggest number of three number is :", numberOne)
if(numberTwo >= numberTwo and numberTwo >= numberThree) :
    print("biggest number of three number is :", numberOne)
else :
    print("biggest number is third and last number", numberThree)


# check number is multiple with 7 or nor


userNumber = int(input("enter your number is 7 multiple or not"))
if(userNumber % 7 == 0) :
     print("your number is allow to multiple 7")
else : 
    print("not allow to number 7")