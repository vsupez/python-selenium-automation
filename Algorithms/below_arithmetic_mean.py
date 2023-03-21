def below_mean(arr):
    sum=0
    result = []

    for n in arr:
        sum+=n

    mean = sum/len(arr)

    for n in arr:
        if n<mean:
            result.append(n)

    return result


test_arr = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_mean(test_arr))
