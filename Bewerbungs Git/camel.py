def main():

    name = input("camelCase: ")


    if "_" in name:
        result = to_camel_case(name)
        print("snake_case: ", result)
    else:
        result = to_snake_case(name)
        print("snake_case: ", result)

def to_camel_case(input_string):
    words = input_string.split("_")
    camel_case_words= [words[0].lower()] + [word.capitalize() for word in words[1:]]
    return "".join(camel_case_words)

def to_snake_case(input_string):

    words = [input_string[0].lower()]
    for char in input_string[1:]:
        if char.isupper():
            words.extend(['_', char.lower()])
        else:
            words.append(char)
    return "".join(words)

if __name__ == "__main__":
    main()