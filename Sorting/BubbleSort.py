# This sorting is the most basic one and uses bubble structure to sort the array

# There are small bubbles of different sizes created and then we traverse through elements 
# swapping the adjacent elements wherever necessary.

def sortIt(arr):
    n = len(arr)

    for i in range(n):

        # To check if there is any swap in the bubble
        swapped = False

        # We keep on reducing the size of the bubble as the last elements are 
        # already sorted

        for j in range(0,n-i-1): 

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True
        
        # If there is no swap in this sized bubble that means it is sorted so we break
        if swapped == True:

            break


if __name__ == "__main__":

    arr = [3,1,4,77,5,21]
    sortIt(arr)
    print(arr)