with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("yes python is present")
else:
    print("python is not present")