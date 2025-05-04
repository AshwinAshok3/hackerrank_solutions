def swap_case(s):
    string = ""
    for i in s:
        if i.islower():
            string += i.upper()
        elif i.isupper():
            string += i.lower()
        else:
            string += i
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
