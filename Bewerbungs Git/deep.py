question = input("what is the answer to the great question of life, the univers and everything? ").strip().lower()

if question == "42":
    print("yes")
elif question == "forty two":
    print("yes")
elif question == "forty-two":
    print("yes")
else:
    print("no")