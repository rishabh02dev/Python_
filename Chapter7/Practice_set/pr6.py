# n! = 1x2x3x4x................xn

# 5! = 1X2x3X4X5

num = int(input("Enter the number : "))
factorial = 1
for i in range (1,num+1):
    factorial = factorial * i 
print(f"The factorial of this number is {factorial}")