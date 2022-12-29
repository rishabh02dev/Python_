words = ["donkey" , "kaddu" , "Moote"]
with open ('sample.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(Word, "####")

    with open ("sample.txt" , "w") as f:
        f.write(content)