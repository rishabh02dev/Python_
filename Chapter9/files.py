#Use open function to read the content of a file.
# f = open('sample.txt' , 'r')
f = open('sample.text')#ydefault the mode is set to r.
# text = f.read()

text = f.read(5) #reads first 5 characters from the file.
print(text)
f.close()