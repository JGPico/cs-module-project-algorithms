'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # loop through array once
    new_arr = []
    for item in arr:
        if item not in new_arr:
            new_arr.append(item)
        else:
            new_arr.remove(item)
    return new_arr[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print()
    print(f"The odd-number-out is {single_number(arr)}")
    print()
