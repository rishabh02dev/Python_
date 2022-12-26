hindi_to_english_dictionary = {
    "Balla" : "bat",
    "geeend" : "Ball",
    "Vastu " : "Item"
}
print("Options are", hindi_to_english_dictionary.keys())
a = input("Enter the hindi Word\n")
print("The meaning of your word is " , hindi_to_english_dictionary.get(a))