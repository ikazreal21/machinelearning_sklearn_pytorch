def pair_sum(nums, target):
    counter = 0
    arr_len = len(nums)
    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            if nums[i] + nums[j] == target:
                print("Pair", i + 1, ": ", end="")
                print(f"({nums[i]}, {nums[j]})")
                counter += 1

    if counter == 0:
        print("Pair not found")


# 1st Test Case
# nums = [8, 7, 2, 5, 3, 1]
# target = 10

# 2nd Test Case
# nums = [5, 2, 6, 8, 1, 9]
# target = 12


pair_sum(nums, target)
