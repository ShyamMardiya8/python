collection = {1,2,3,4}
secondCollection = {1,2,2,2,"hello", "hello", "world"}
print(type(collection))
print(secondCollection)

# note : set using to all duplicate value is removed and not showing duplicate value length
print(len(secondCollection))

# how to create empty set and how to declare
null_set = set()
print(type(null_set), null_set)


# set methods 
null_set.add(1)
null_set.add(2)
null_set.add(3)
# null_set.remove(2)
# null_set.clear()
null_set.pop() 
# if remove random value to use pop
print("remove all value in set :",null_set)


# union in python union means you have two set and bot set in unique value is only return

set1 = {1,2,3}
set2 = {3,3,4}
print(set1.union(set2))

# not it is only work in shallow copy not change original value 


# second is 2 set in common value menas same value return in intersection method using set
print(set1.intersection(set2))


# practice 

sub = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(len(sub))

nine = {9, float(9.0)}
print(nine)