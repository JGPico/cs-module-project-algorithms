'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here

    length = len(nums)
    new_arr = []

    if k >= length or k <= 0:
        return "Window is too big"

    for i in range(length - k + 1):
        mini_arr = []
        for j in range(k):
            mini_arr.append(nums[j + i])
        new_arr.append(max(mini_arr))

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    expected = [3, 3, 5, 5, 6, 7]
    k = 3

    print()
    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    print()
