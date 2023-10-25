# Helen Zhang
# encode 6-digit password shift up 3 num
def encoder(string):
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
    print(encoder("12345555"))
    print(encoder("00009962"))


if __name__ == '__main__':
    main()

