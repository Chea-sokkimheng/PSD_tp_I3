# Problem 1. Student Profile Card  

name = "Piheng"
age = 20
major = "Data Science"
gpa = 3.67
is_scholar = True

print("Student Profile Card")
print("====================")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"GPA: {gpa:.2f}")
print(f"Scholarship Student: {is_scholar}")
print("====================")

print(f"'{name}' -> {type(name).__name__}")
print(f"'{age}' -> {type(age).__name__}")
print(f"'{major}' -> {type(major).__name__}")
print(f"'{gpa}' -> {type(gpa).__name__}")
print(f"'{is_scholar}' -> {type(is_scholar).__name__}")

age = "20"
print(type(age))