def is_mountain(arr):
    # low_peak = False
    # high_peak = False
    #
    # for i in range(len(arr)):
    #     if i == 0: continue
    #     if arr[i] >= arr[i - 1]:
    #         high_peak = True
    #     else:
    #         if high_peak == True and arr[i] < arr[i - 1]:
    #             return True
    #
    # return False

#Vitaly's solution
    i=1
    while i<len(arr) and arr[i]>arr[i-1]:
        i+=1
    if i==1 or i==len(arr):
        return False

    while i<len(arr) and arr[i]>arr[i-1]:
        i+=1

    if i==len(arr):
        return True
    return False




test_arr = [1,2,4,2,3]
result = is_mountain(test_arr)
print(result)
