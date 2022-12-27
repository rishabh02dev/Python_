#printing the table for 5
num = int(input("Enter the number\n"))
for i in range(1,11):
    print(str(num) + " X " + str(i) + "=" + str(i*num))
    print("Another method")
    print(f"{num}X{i} = {num*i}")