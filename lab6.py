# Helen Zhang
# encode 6-digit password shift up 3 num
def encode(string):
    pw = ""
    for c in string:
        if c == "9":
            pw += "2"
        elif c == "8":
            pw += "1"
        elif c == "7":
            pw += "0"
        else:
            pw += str(int(c) + 3)
    return pw


def main():
    ongoing = True
    while ongoing:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print()
        option = input(print("Please enter an option: "))

        if option == 1:
            password = input(print("Please enter your password to encode: "))
            storedpw = encode(password)
            print("Your password has been encoded and stored!")

        if option == 2:
            print("The encoded password is " + decode(storedpw) + ", and the original password is " + storedpw)

        if option == 3:
            ongoing = False


if __name__ == '__main__':
    main()

