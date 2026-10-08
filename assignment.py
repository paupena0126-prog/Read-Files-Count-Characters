# CIS 3330 - CODE 3
# Use file_content variable to conduct your analysis


file_content = open('Office_Products_Modified.txt').read()


def get_number_of_a():
    total = 0
    for letter in file_content:
        if letter.lower() == "a":
            total += 1
    return total        


def get_number_of_z():
    total = 0
    for letter in file_content:
        if letter.lower() == "z":
            total += 1
    return total        


def get_number_of_percent():
    total = 0
    for character in file_content:
        if character == "%":
            total += 1
    return total        


def get_number_of_char(user_char):
    total = 0
    for character in file_content:
        if character.lower() == user_char.lower():
            total += 1
    return total        


# Test your code below, inside the if statement
if __name__ == "__main__":
    print("Number of A's:", get_number_of_a())
    print("Number of Z's:", get_number_of_z())
    print("Number of % symbols:", get_number_of_percent())
    print("Number of E's:", get_number_of_char("e"))
