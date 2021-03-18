year = int(input("Please Enter a Year to Calculate How Many Days are in February of Given Year - "))
message = ""
if year > 0:
    message = "In " + format(year) + ", February has "
    if year % 100 == 0:
        if year % 400 == 0:
            message += "29"
        else:
            message += "28"
    else:
        if year % 4 == 0:
            message += "29"
        else:
            message += "28"
    message += " days."
else:
    message = "Invalid Year Entered"
print(message)