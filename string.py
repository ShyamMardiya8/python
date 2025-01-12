# how to start value in new line 
string = "hello \n my name is shyam"
#  how to get tab space apply
stringTab = "\thello"
print(string)
print(stringTab)

# how to find length of string
print("length is :", len(string))

# indexing is how to work in python


name = "shyam"
# print(name[0])
print(name)
# print(name[0] == "h")

# slice in python


value = "one two three"
print(value[8 : len(value)])
# second method to get last value of string 
print(value[8:])
print(value[:4])


# negative value indexing in slice of python

fruit = "apple"
print("negative indexing is :", fruit[:-3])



# string more function 

valueStr = "my name is shyam"
valueStr = valueStr.capitalize()
print("1st charcter capitalize is :", valueStr)
print("old value convert into new value :", valueStr.replace("is", "Is"))
print("find index of string using find method in python :",valueStr.find("shyam"))
print("how to find value in program how many time is exit to find use count :", valueStr.count("m"))


# practice program for python in string and string methods 

valueF = input("enter a any number to find the length of the string value :")
print("your string value length is :", len(valueF))