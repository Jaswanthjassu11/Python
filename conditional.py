# one year is divisible by 400 is leapyear
# one year is divisible by 100 but with 400
#     one year isdivisible by 4

# year = int(input("enter the number:"))
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("not a leap year")

# n = 15
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")
# a = 14
# if a>10 and a % 2 == 0:
#     print("greater than 0 and even even number")
# else:
#     print("no")
# triangle1= int(input("enter the angle:"))
# triangle2= int(input("enter the angle:"))
# triangle3= int(input("enter the angle:"))
#
# if triangle1+triangle2+triangle3 == 180:
#     print("equivalent triangle")
# else:
#     print("not a equivalent triangle")
# day = int(input("enter the number:"))
# if day == 1:
#     print("monday")
# elif day == 2:
#     print("tuesday")
# elif day == 3:
#     print("wednesday")
# elif day == 4:
#     print("thursday")
# elif day == 5:
#     print("friday")
# elif day == 6:
#     print("saturday")
# elif day == 7:
#     print("sunday")
# else:
#     print("no day")
#

#     electricity


"""
100units - 5rs
101 - 200 - 7rs
201 ... - 10rs"""


units = int(input("Enter your units:-\t"))

if units <= 100:
    print(f"your current bills is {units * 5}")

elif 100 < units <= 200:
    print(f"you're cuurent bill is {100 * 5 + (units -100) * 7}")

if 200 < units <= 999999999999999:
    print(f"you're current bill is {100 * 5 + 100 * 7  + (units - 200) * 10}")