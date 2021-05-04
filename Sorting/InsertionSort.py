# Here we have to keep on taking the minimum number to the left

# This sort is only good with small arrays or arrays which are almost sorted

# Time Complexity - O(n^2)

# Space Complexity - O(1)

def insertionSort(arr):

    # We iterate from the element at index 1 because we will be comparing with the numbers to the left

    for i in range(1,len(arr)):


        key = arr[i] #We store the value we are comparing in key so that we don't loose it while swaping

        j = i-1 # This will help us keep track of the numbers to the left

        while j >= 0 and key < arr[j]: # this loop runs and swaps as far as the number to the right is less than that of left

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key




if __name__ == "__main__":

    arr = [5, 11, 12, 13, 6]
    insertionSort(arr)

    print(arr)


''' For understanding purpose:

When we have i = 3 we have reached this array - [11,12,13,5,6] now we want that five to be compared and reach the very left so the above algorithm will work as

key = 5
j = 2

-> [11,12,13,13,6]  ------- j = 1
-> [11,12,12,13,6]  ------- j = 0
-> [11,11,12,13,6]  ------- j = -1

and then we finally put the key in one place ahead of the place we stopped j i.e at index 0

[5,11,12,13,6]

Similar we do with 6 and we get it sorted

'''