# TO-DO: Complete the selection_sort() function below
# a = [4, 3, 1, 2, 6, 5]


def selection_sort(arr):
    # Start with current index = 0
    # For all indices EXCEPT the last index: n-1
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(arr)
        # a. Loop through elements on right-hand-side of current index and find the smallest element
        for x in range(cur_index + 1, len(arr)):
            # TO-DO: find next smallest element(hint, can do in 3 loc)
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # b. Swap the element at current index with the smallest element found in above loop
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr
# print(selection_sort(a))


# TO-DO:  implement the Bubble Sort function below
#arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def bubble_sort(arr):
    # in a worse case scenario, we need n-1 passes through the collection for every element to “bubble up” to its correct position.
    # Loop through your array
    for i in range(0, len(arr)):
        print(arr)
        for x in range(0, len(arr)-1):
            # Compare each element to its neighbor
            if arr[x] > arr[x + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[x], arr[x+1] = arr[x+1], arr[x]

        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    return arr


# print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


strings = ["Google", "Apple", "Microsoft"]


def sort_length(arr):
    for i in range(0, len(arr)):
        print(arr)
        for x in range(0, len(arr)-1):
            if len(arr[x]) > len(arr[x+1]):
                arr[x], arr[x+1] = arr[x+1], arr[x]

    return arr


print(sort_length(strings))
