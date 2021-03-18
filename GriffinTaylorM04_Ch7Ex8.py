print("Name Search by Taylor Griffin")
# I should've been using comments from the start, debugging sucks without them!
# Variables
output = ""
gender = ""
# Gender Selection loop
while gender != "boy" and gender != "girl" and gender != "both":
    gender = input("Enter 'boy', 'girl', or 'both' : ")
    if gender != "boy" and gender != "girl" and gender != "both":
        print("Invalid Input Detected!")
if gender == "both":
    is_both = True
else:
    is_both = False
finished = False
while not finished:
    if is_both:
        if gender == "both":
            gender = "boy"
        else:
            gender = "girl"
            output = output + "\n"
            finished = True
    else:
        finished = True
    name = input("Enter a " + gender + "'s name: ")
    text_file = open(gender + 'Names.txt', 'r')
    conditional_not = 'not '
    for popular_name in text_file:
        if popular_name.rstrip('\n') == name:
            conditional_not = ''
    text_file.close()
print(output + name," is ", conditional_not , " a popular ", gender, "'s name")
