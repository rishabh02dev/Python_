f = open('./Practiceset/Poem.txt')
t = f.read()
if 'twinkle' in t:
    print("yes twinkle is find")
else:
    print("twinkle is not found")
f.close()