if __name__ == '__main__':
    # alphanum
    s = input()
 
    # alphanumeric
    print(any(char.isalnum() for char in s))

    # alphabetic
    print(any(char.isalpha() for char in s))

    # digits
    print(any(char.isdigit() for char in s))

    # lowercase
    print(any(char.islower() for char in s))

    # uppercase
    print(any(char.isupper() for char in s))
