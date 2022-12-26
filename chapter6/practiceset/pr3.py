comment = input("ENter the text")
if("make a lot of money" in comment):
    spam = True
elif("buy now " in comment):
    spam = True
elif("click this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("this text is not spam")