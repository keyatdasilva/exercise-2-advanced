# Question 1
import math
a = 5 
b = 10
c = 7

a += 3
b *= 2
c %= 4

square = a**2 + b**2 + c**2 
square_root = math.sqrt(square)
rounded_square = round(square_root, 2)

print(rounded_square)

# Question 2 
x = 10 
y = 4
z = 2 

condition_1 = x > y 
condition_2 = y % 2 == 0
condition_3 = z <= x 
final_condition = condition_1 or (condition_2 and condition_3)
print(final_condition)

# Question 3
score = int(input("Enter your test score:"))
if score >= 90 :
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score > 60:
    grade = "D"
else :
    grade = "F"
    
print(grade)

# Question 4
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operation = input('Enter operation:(+,-,*,/,sqrt,%)')

if operation == "+": 
    result = num1 + num2 
elif operation == "-" :
    result = num1 - num2
elif operation == "*":
    result = num1 * num2 
elif operation == "/":
    if num2 == 0:
      result = "cannot divide by 0"
    else: 
        result = num1/num2 
elif operation == "%":
    if num2 == 0 :
     result = "cannot divide by 0"
    else : 
       result = num1 % num2 
elif operation == "**": 
    if num1 == 0 :
     result = "cannot divide by 0" 
elif operation == 'sqrt':    
   if num1 < 0:
      result = "cannot take the square root of a negative number" 
   else: 
      result = num1 ** 0.5  
else: "Invalid operation"
print(result)
