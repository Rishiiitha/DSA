a=int(input())
match (a):
    case 1:
        print("sunday")
    case 2:print("monday")
    case 3:print("tuesday")
    case 4:print("wednesday")
    case 5:print("thursday")
    case 6:print("friday")
    case 7:print("saturday")
    case _ : print("not a valid day")
print("have a long nice day and an icecream :)")