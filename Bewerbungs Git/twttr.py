question = input("Input: ")

vowls = ["a", "e", "i", "o", "u", "A", "E","I","O","U"]

result= ""

for char in question:
    if char not in vowls:
        result +=char

print(result + "\n")