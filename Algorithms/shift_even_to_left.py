
def reorder(arr: list):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if i == 0:
                continue
            else:
                # Swap even element with odd, bring it in the front
                j = i
                while j != 0:
                    if arr[j - 1] % 2 != 0:
                        arr[j - 1] = arr[j - 1] + arr[j]
                        arr[j] = arr[j - 1] - arr[j]
                        arr[j - 1] = arr[j - 1] - arr[j]
                    j -= 1

    return arr


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
test_result = reorder(test_list)
print(test_result)
