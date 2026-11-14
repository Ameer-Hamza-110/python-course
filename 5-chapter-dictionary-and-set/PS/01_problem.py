dictionary = {
    "Paisa": "Money",
    "Dost": "Friend",
    "Dil": "Heart",
    "Zindagi": "Life"
}


userINput = input("Enter a word to get its meaning: ")

print("the meaning of", userINput, "is:", dictionary.get(userINput, "Word not found in the dictionary."))