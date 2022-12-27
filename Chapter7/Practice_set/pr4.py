num = int(input("Enter the given number"))
prime = False
for i in range(2,num):
    if (num%i ==0):
      prime = True
      break
else:
    print("The number is prime")