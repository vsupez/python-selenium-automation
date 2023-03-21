def two_lowest_elements(arr):
    min_arr = []

    min_num = min(arr)
    min_arr.append(min_num)
    arr.pop(arr.index(min_num))

    min_num = min(arr)
    min_arr.append(min_num)

    return min_arr


test_arr = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest_elements(test_arr))
