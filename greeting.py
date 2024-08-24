def greeting(userName):
    print("Hello,", userName)


def full_name(first_name, last_name):
    return first_name + " " + last_name


def main():
    first_name = input("What's your given name?\n")
    last_name = input("What's your surname?\n")
    greeting(full_name(first_name, last_name))


main()

