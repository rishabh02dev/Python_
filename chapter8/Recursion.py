# n! = 1*2*3*4*5*6.........*n

#Recursive is a function which calls itself It is used to directly use a mathematical formula as a function.

n= 4
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

# dry run
# 1*1*1*2*1*3*1*4
# 2*3*4
# 6*4
# 24

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial_iter(0)
print(f)

def factorial_recursive(n):
    if n ==1 or n ==0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)