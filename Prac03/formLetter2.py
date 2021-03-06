__author__ = 'Smoo'


def printCurrency(value):
    print("$" + format(value, ".2f"))


def displayStart(salutation, name, donation):
    print("Hello", salutation, name + ",")
    print("We would like to thank for your recent donation of ", end="")
    printCurrency(donation)
    print(name + ",", "your support is much appreciated!")


def displayEnd(closing):
    print()
    print(closing)
    print("The CP1200 Team")


def main():
    print("-- Form Letter --")
    salutation = input("Salutation: ")
    name = input("Name: ")
    donation = float(input("Donation: "))
    if donation > 1000:
        closing = "Best regards,"
    elif donation < 10:
        closing = "Cheers,"
    elif donation >= 10 or donation <= 1000:
        closing = "Thanks,"

    displayStart(salutation, name, donation)
    displayEnd(closing)


main()