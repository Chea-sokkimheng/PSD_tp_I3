#PROBLEM 7
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        # digit = n % 10
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def is_palindrome(n):
    return n == reverse_number(n)

numbers = [2026, 12321, 9875]

for n in numbers:
    print(n, ":digit sum =", digit_sum(n), 
          ", reversed =", reverse_number(n), 
          ", is palindrome =", is_palindrome(n))

count = 0
for n in range(10, 1000):
    if is_palindrome(n):
        count += 1

print(f"Number of palindromes from 10 to 999: {count}")