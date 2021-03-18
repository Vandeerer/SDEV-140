print("Character Analysis by Taylor Griffin")
def check(string):
    lowercase = 0
    uppercase = 0
    digits = 0
    whitespace = 0
    other = 0
    low = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    upper = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    digit = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    whiteSpace = ' '
    for n in string:
        if n in low:
            lowercase += 1
        elif n in upper:
            uppercase += 1
        elif n in digit:
            digits += 1
        elif n in whiteSpace:
            whitespace += 1
        else:
            other += 1
    print("Uppercase: " + str(uppercase).ljust(7))
    print("Lowercase: " + str(lowercase).ljust(7))
    print("Digits: " + str(digits).ljust(7))
    print("Whitespace: " + str(whitespace).ljust(7))
with open('text.txt', 'r') as file:
    data = file.read()
check(data)
