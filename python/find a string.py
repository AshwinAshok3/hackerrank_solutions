'''
ABCDCDC
CDC
'''
def count_substring(string, sub_string):
    a = len(string)-len(sub_string)
    b = 0
    for i in range(a+1):
        if sub_string == string[i:len(sub_string)+i]:
            b+=1
    return b

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
