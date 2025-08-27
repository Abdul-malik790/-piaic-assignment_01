# take a two numbers as input form the user 
# print their sum
# print whether the first number is greater than the second number or not

# solution :
# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Calculate and print the sum
sum_result = num1 + num2
print("Sum of the two numbers:", sum_result)
# Check and print whether the first number is greater
if num1 > num2:
    print("The first number is greater than the second number.")
else:
    print("The first number is NOT greater than the second number.")

