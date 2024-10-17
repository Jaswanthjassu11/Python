a = 5
b = 2

temp = a
a = b
b = temp

print(f"b ={b} a = {a}")


a = "1" # STR
print(2 + int(a))


a = 10
b = 5


username = "bharath@gmail.com"
password = 1233455678

print(f"username : {username}, password : {password}")


#  if - else

#   comparison operators   - True/ False

print(a > b)

print(a == b)

print(a != b)

print(a >= b)


print(a <=b )


# logical operators


# and
# or
# not

# print(a > b and a < b)


print(not (a >b))



#    if - else

# age = int(input("enter the age:"))
#
# if age>=18:
#     print("you eligible to roller coaster")
# else:
#     print(f" come after  = {18 - age} years")

#
# age = int(input("enter the number:"))
# if age >= 0 and age <= 18:
#     print("you are a junior")
#
# elif age > 18 and age <= 40:
#     print("you are an adult")
#
# elif age>40 and age<=60:
#     print("you are a senior")
# elif age<0:
#     print("invalid age")
# else:
#     print("close to dead")

# a = 15
# b = 20
# print(a+b)
# a = 15
# print(a%2)
# a = 15
# print(type(a))
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# print(num1+num2/2)
# a = 34
# b = 60
# print(a>b)
# print(a*
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# num3 = int(input("enter the third number:"))
# num4 = int(input("enter the fourth number:"))
# if num1 >num2 and num1 > num3:
#     print("num1 is greater:")
# elif num2>num3 and num2>num1:
#     print("num2 is greater:")
# elif num3 >num1 and num3>num2:
#     print("num3 is greater:")
# subject1 = int(input("enter the number1:"))
# subject2 = int(input("enter the number2:"))
# subject3 = int(input("enter the number3:"))
#
# total_percent = ((subject3+subject2+subject1)/300) * 100
#
# # print(total_percent)
#
# if (subject1 /100) * 100 >= 33 and (subject2 /100) * 100 >= 33 and (subject3/100 ) * 100>= 33 and total_percent >= 40:
#     print("you passed")
# else:
#     print("You're failed")

# user_name= "bharat kumar reddy"
# b = len(user_name)
# print(b)
#
# if b >10:
#     print("yes")
# else:
#     print("no")
# student_marks=int(input("enter the marks:"))
#
# if 90 <= student_marks <= 100:
#     print("10 points")
# elif 80 <= student_marks <90:
#     print("9 points")
# elif 70 <= student_marks <80:
#     print("8 points")
# elif 60 <= student_marks <70:
#     print("7 points")
# elif 50 <= student_marks <60:
#     print("6 points")
# else:
#     print("fail")




#   Loops

# 1 , for loop
#  2. while loop
#  3. do while loop


# n = int(input("Enter the number:-"))
# for i in range(n):
#     if i % 2== 0:
#         print("Even")
#     else:
#         print("Odd")


# for i in range(10):
#     for j in range(i):
#         for k in range(j):
#             print(i, j, k)




#   while loops


# problems

#  sum of nn natural numbers

# sum = 0

# n = int(input("Enter a number:-"))

# for i in range(1, n+1):
#     sum += i
#
# print(sum)


#   Factorial


# 5!= 5 * 4 * 3 * 2 * 1

# fact = 1
#
# for i in range(1, n+1):
#     fact *= i
#
# print(fact)


#   Multiplication table
#
# """
# 10 * 1 = 10
# 10 * 2= 20
# .
# .
# .
# .
# .
# 10 * 10 = 100
# """

# num = 10
#
# for i in range (1,num+1):
#     print(f"{num} * {i} = {num * i}")

# x = 0
# while ( x < 10):
#     print(x)
#     x +=1

# def prime(num):
#     if num > 0:
#         for i in range(2 , num):
#             if num % i == 0:
#                 return "not a prime number"
#         return "prime number"
# print(prime(21))

# sum = 0
# for i in range(1,11):
#     sum +=i
#
# print(sum)

# fact = 1
# for i in range(1,6):
#     fact *=i
#
# print(fact)


#   star pattern

n = 3

for i in range(n):
    for j in range(2 * i + 1):
        print("*", end="")
    print()

print()

for i in range(1,n +1):
    for j in  range(i):
        print("*",end="")
    print()














