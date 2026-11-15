phrase = input("Фраза: ")
if phrase == "":
    print("Слов: 0")
else:
    spaces = 0
    for char in phrase:
        if char == " ":
            spaces += 1
    print(f"Слов: {spaces + 1}")
