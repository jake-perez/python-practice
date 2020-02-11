def rgb_sort(arr):
    r_index = 0
    b_index = len(arr)-1

    for i in range(0, len(arr)):
        if i <= b_index:
            if arr[i] == 'R':
                swap(arr, i, r_index)
                r_index += 1
            if arr[i] == 'B':
                swap(arr, i, b_index)
                i -= 1
                b_index -= 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
