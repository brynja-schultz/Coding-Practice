def swap_case(s):
    string = ""
    for i in range(len(s)):
        if s[i].islower():
            string += s[i].upper()
        else:
            string += s[i].lower()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
