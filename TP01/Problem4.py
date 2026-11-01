# PROBLEM 4
# Part A
print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))

#Part B
def safe_int(text):
    try:
        return int(float(text.strip()))
    except ValueError:
        return None

for sample in ["42", "-8", "3.9", "abc", ""]:
    print(f"{repr(sample)} -> {safe_int(sample)}")
    
#Part C
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

a = safe_int(num1)
b = safe_int(num2)

if a is not None and b is not None:
    print("Sum =", a + b)
else:
    print("Please enter valid numbers.")