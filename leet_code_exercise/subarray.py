def small_subarr(arr, k):
    arr_len = len(arr)
    min_len = arr_len + 1
    for start in range(0, arr_len):
        curr_sum = arr[start]
        if curr_sum > k:
            return 1
        for end in range(start + 1, arr_len):
            curr_sum += arr[end]
            if curr_sum > k and (end - start + 1) < min_len:
                min_len = end - start + 1
    return min_len


arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 40

arr_len = len(arr)

res = small_subarr(arr, k)
if res == arr_len + 1:
    print("No subarray exists")
else:
    print(f"The smallest subarray length is {res}")
