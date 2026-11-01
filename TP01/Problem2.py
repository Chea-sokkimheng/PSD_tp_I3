# Problem 2. Time Converter  
total_second = 9875
hours = total_second // 3600
minutes = (total_second % 3600) // 60
seconds = total_second % 60 

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

check = hours * 3600 + minutes * 60 + seconds
print(f"Check: {check == total_second}")
