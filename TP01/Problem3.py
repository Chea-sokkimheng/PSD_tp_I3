#PROBLEM 3
def celsius_to_fahrenheit(c, round_to=1):
    f = c * 9 / 5 + 32
    return round(f, round_to)

def fahrenheit_to_celsius(f, round_to=1):
    c = (f - 32) * 5 / 9
    return round(c, round_to)

print("celsius | fahrenheit")
print("-----------|----------")

for c in range(0, 101, 20):
    print(c, "|", celsius_to_fahrenheit(c))

print("98.6 F =", fahrenheit_to_celsius(98.6), "C")

f= celsius_to_fahrenheit(37)
c= fahrenheit_to_celsius(f)

print("37 C =",f, "F")
print(f, "F=", c, "C")

# print(celsius_to_fahrenheit(25, round_to=3))


  