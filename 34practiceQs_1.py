# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# result = [ ]    
# for i in range(x+1):
#     for j in range(y+1):
#         for z in range(z+1):
                
#                 if i+j+z != n:
#                      result.append([i,j,z])
                     
# print(result)

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))
# n = int(input("Enter n: "))

# # Using list comprehension to generate the desired list of coordinates
# result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# print(result)
import calendar

# Read the input date
month, day, year = map(int, input().split())

# Get the weekday as an integer (0=Monday, 1=Tuesday, ..., 6=Sunday)
weekday_int = calendar.weekday(year, month, day)

# List of days in uppercase corresponding to the integers returned by calendar.weekday
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# Get the corresponding day name
day_of_week = days[weekday_int]

# Print the day of the week
print(day_of_week)
