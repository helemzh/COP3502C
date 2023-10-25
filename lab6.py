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
    stored = ""
    ongoing = True

    while ongoing:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            stored = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            print("The encoded password is " + decode(stored) + ", and the original password is " + stored)

        elif option == 3:
            ongoing = False
        print()


if __name__ == '__main__':
    main()

