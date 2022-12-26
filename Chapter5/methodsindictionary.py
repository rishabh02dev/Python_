myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 3, 4, 5],
    "AnotherDict": {"harry": "Player"},
    1:2
}
#DICTIONARY METHODS
print(myDict.keys()) #prints the keys of the dictionary

print(myDict.values())

print(myDict.items())

print(myDict)
updateDict = {
    "rishuu": "rishabh's nickname",
    "REACT" : "Framework"

}
myDict.update(updateDict) #updates the dictionary by adding key value paris from updatedict
print(myDict)

print(myDict.get("rishuu"))

#in order to get the particular element it's better to you .get as it doesn't throw error.
