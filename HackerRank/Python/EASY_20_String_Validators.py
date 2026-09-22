if __name__ == '__main__':
    s = input()
    # check alphanumeric
    print(any(char.isalnum() for char in s))
    # check alphabetical
    print(any(char.isalpha()for char in s))
    # check digits
    print(any(char.isdigit() for char in s))
    # check lowercase
    print(any(char.islower() for char in s))
    # check uppercase
    print(any(char.isupper() for char in s))
