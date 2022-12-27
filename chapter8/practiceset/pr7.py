def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this = "   rishabh is a good coder."
n = remove_and_split(this, "rishabh")
print(n)