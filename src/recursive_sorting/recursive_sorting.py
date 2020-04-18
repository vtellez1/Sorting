# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    iA = 0
    iB = 0

    for i in range(0, elements):
        if iA >= len(arrA):
            merged_arr[i] = arrB[iB]
            iB += 1
        elif iB >= len(arrB):
            merged_arr[i] = arrA[iA]
            iA += 1
        elif arrA[iA] < arrB[iB]:
            merged_arr[i] = arrA[iA]
            iA += 1
        else:
            merged_arr[i] = arrB[iB]
            iB += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # 1. While (We'll need to loop) your data set contains more than one item, split it in half
    if len(arr) > 1:
        half = len(arr)//2
    # 2. Once you have gotten down to a single element, you have also *sorted* that element
    # (a single element cannot be "out of order")
        first_half = merge_sort(arr[:half])
        sec_half = merge_sort(arr[half:])
        arr = (merge(first_half, sec_half))

    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
    return arr


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
