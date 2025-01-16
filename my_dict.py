di = {
    "name" : "Shyam",
    "age" : 17,
    "subject" : ["mathes", "science", "English"],
    "tupple" : ("one", "two", "three")
}
print(di["subject"])
# how to change value in dict 
di["age"] = "19"
print(di)
print(type(di))
print(di["tupple"][0])


# created nested dict

info = {
    "name" : "shyam",
    "friends" :{
        "name" : "manthan",
        "secondName" : "vasu",
    },
}
print(info["friends"]["secondName"])

# dict method apply in dict


print("keys Method to get keys and convert into list:",list(info.keys()))
print("values Method :", list(info.values()))
print("item method to get keys and values both :", list(info.items()))
print("item get to helping key", type(str(info.get("name"))))
print("inner dict value :", list(info["friends"].values()))
print("how to add new value in dict using update method", info.update({"age" : "19"}))
print("dict", info)



# practice set dict


infoWord = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal"
}
print(infoWord["table"])


marks = {}
marks.update({(input("enter subject name :"),
  input("enter subject one marks :"))})
marks.update({(input("enter subject name :"),
  input("enter subject one marks :"))})
marks.update({(input("enter subject name :"),
  input("enter subject one marks :"))})
print(marks)

