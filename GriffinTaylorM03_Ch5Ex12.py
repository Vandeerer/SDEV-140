print("Maximum of Two Values - Taylor Griffin")
def max(firstValue, secondValue):
    if firstValue > secondValue:
        return firstValue
    else:
      return secondValue
def getValuesFromUser():
    userFirstValue = int(input("Input the first value "))
    userSecondValue = int(input("Input the second value "))
    return userFirstValue, userSecondValue
def main():
  userFirstValue, userSecondValue = getValuesFromUser()
  print("Maximum between",userFirstValue, "and", userSecondValue, "is", max(userFirstValue, userSecondValue))
main()
