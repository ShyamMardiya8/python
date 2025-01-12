nimber = 7
name = "shyam"
address = "Mota varachha"
print(type(nimber))
print(type(name))
print(type(address))


# practice of calculation in py

# a = 1
# b = 2
# print( a + b)


a = 1
b = 2
c = a + b
c+=10
print(c == 4)
print(c != 4)
print(a >= b)
print(c)
print(not True)
print(not False)


# and operator and or opeartor in py
value = True
valueTwo = False
print("check value bollean values :", value and valueTwo)
print("check value bollean values :", value or valueTwo )
print("check variable value using this ", a == b and b == a)
print("check variable value using this ", a == b or b != a)


# type conversion
 
value1 = 2
value2 = 2.5

# type cast method means manually change value type using int and float keyword names
value3 = "3.5"
value4 = float(value3)

print(value4)
print(type(value4))
sum = a + b



# input get from user and make sum 

firstNumber = input("enter a your first number : ")
secondeNumber = input("enter b your second number : ")
answer = print(int(firstNumber) + int(secondeNumber))

# practice write 2 floating values and find their average


num1 = float(input("enter your first number :"))
num2 = float(input("enter your second number :"))

print("avg value is :",(num1 + num2) / 2)
print("a is greater than b ", num1 >= num2)

