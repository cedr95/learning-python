# exercise 1 List manipulation

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.sort()
print(fruits)


# Excercise 2 Dictionary basics

student = {"name": "John Doe", "age": "25", "major": "CS"}

student["major"] = "EE"
student["year"] = "Senior"
print(student.keys())
print(student.values())


# Exercise 3 List of dictionaries

dictionaries = [{"title": "Yeeee", "author": "CD", "year": 2024}, {"title": "Yeeeesss", "author": "CDD", "year": 2054}, {"title": "Yeeeesssir", "author": "CDEEEZ", "year": 2026}]

print(dictionaries[1]["title"])
print(dictionaries[2]["year"])

for i in range(len(dictionaries)):
    print(dictionaries[i]["author"], dictionaries[i]["title"])

# Exercise 4: dictionary containing a list

courses = {"math":["Jay","Chris","Evab"], "science": ["Chris","Jake", "Amy"], "history": ["Tasia", "Andy","Khoa"]}
print(courses.keys())
for i in range(5):
    courses["math"].append("J")

courses["history"].pop(-1)
print(courses["science"])
courses["physics"] = ["This", "Is", "not", "bad"]
print(courses.keys())
print(courses.items())