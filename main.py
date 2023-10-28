# Andy Hagen
# COP3502C
# UFID: 82680804


def encode(password):
    # Create an empty string assigned to a new variable to store the encoded password
    encoded_password = ""

    # Check if password is 8 digits
    if len(password) == 8:
        for i in range(0, len(password)):
            encoded_digit = int(password[i]) + 3
            encoded_password += str(encoded_digit)
    else:
        print("Be sure your password is 8 digits!")

    # Return encoded password string
    return encoded_password


def main():
    # Menu
    print("Menu\n-------------")
    print("1. Encode\n2. Decode\n3. Quit")

    # While loop to make a looping menu
    while True:
        option = int(input("Please enter an option: "))

        # Encode password option
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

            # Menu
            print("Menu\n-------------")
            print("1. Encode\n2. Decode\n3. Quit")

        # Decode password option
        if option == 2:
            # Print decoded password here.
            pass

        # Quit looping menu option
        if option == 3:
            # Break the loop
            break


if __name__ == '__main__':
    main()
