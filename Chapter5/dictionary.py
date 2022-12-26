myDict = {
    "Fast" : "In a Quick Manner",
    "Harry" : "A Coder",
    "Marks" : [1,2,3,4,5],
    "AnotherDict" : {"harry" : "Player"}
}

print(myDict["Fast"])
print(myDict["Harry"])
myDict["Marks"] = [45,45,45]
# it overwrites the current key 
print(myDict["Marks"])
print(myDict["AnotherDict"]["harry"])