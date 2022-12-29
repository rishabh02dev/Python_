with open("log.txt") as f:
    while content:
    
        content = f.readline()

if 'python' in content.lower():
    print("yes python is present")
else:
    print("python is not present")