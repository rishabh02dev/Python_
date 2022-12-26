s = set()
s.add(20)
# s.add(20.0) in python 20.0 and 20 are counted as one only
s.add("20")
print(len(s))