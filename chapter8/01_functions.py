marks = [45, 78, 86, 77]
percentage1 = (sum(marks)/400)*100

marks2 = [75, 98, 88, 78]
percentage2 = (sum(marks2)/400)*100
print(percentage1 , percentage2)

#Another approach this is the long and basic approach which written without using functions

marks = [45,78, 86, 77]
percentage1 = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

marks2 = [75, 98, 88, 78]
percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100
print(percentage1, percentage2)

def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)

print(percentage1, percentage2)

def function():
    print("Hello rishuu")


#creating some random functions for better understanding
function()

def function():
    print("Hello Noobitaaaaaa")

function()

name = input("Enter your name sir\n")
def function():
    print("hello dear user "  + name)

function()

