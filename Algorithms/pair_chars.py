str = "abc"

def return_two_chars(str):
    str_arr = []
    if len(str)%2!=0:
        str += " "

    for i in range(len(str)-1):
        str_arr.append(str[i:i+2])

    return str_arr


print(return_two_chars("abcdef"))