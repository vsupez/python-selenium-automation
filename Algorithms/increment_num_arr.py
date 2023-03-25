
def increment_num(arr: list):
    number = 0
    new_arr = []
    for n in arr:
        number = number * 10 + n % 10

    number += 1

    while number != 0:
        digit = number % 10
        new_arr.append(digit)
        number = number // 10

    new_arr.reverse()
    return new_arr


test_list = [1,2,9]
test_result = increment_num(test_list)
print(test_result)