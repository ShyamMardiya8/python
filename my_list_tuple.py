student = ["manthan", "vasu", "shyam", "jenish"]
student[0] = "vaibhav"
print(student[0])
print(student)
print("length", len(student))

# slice in python

print(student[3:])
print("adding negative to slice value in list", student[:-3])

# list methods 

student.append("pinak")
print("after adding one student add in class ", student)

# list in adding sort method using python
student.sort()
print("after student list sorting", student)

# list and value adding reverse
student.sort(reverse=True)
print("after reversing value using sort and reverse parameter : ", student)

student.reverse()
print("reverse value python reverse inbuild method",student )

# insert value using index in python

student.insert(0, "john")
print("after 0 index in value is enter than using insert method :", student)


# tuple in python step mby step

tup = (1,2,3,2)
print(tup[0])

# how to find index of value in tupple
print(tup.index(3))
# how many time value is return same to same to get using count method using tupple method
print("value is geeting in the tupple times :",tup.count(2))



# practice questions 

movies = []
movies.append(input("enter a first movie names"))
movies.append(input("enter a second movie names"))
movies.append( input("enter a third movie names"))

# movies.append(movieOne)
print("your movie names is ", movies)


# find list in value is palidrom

ls = [1, "abc", "abc", 2]
ls2 = ls.copy()
ls.reverse()
if(ls == ls2):
    print("it is palidrome")
else : 
    print("it is not palidrome")


# find a is how many time in tupple

# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))


# store value in a to d and sort the value

alha = ["D", "B", "C", "A"]
alha.sort()
print(alha)