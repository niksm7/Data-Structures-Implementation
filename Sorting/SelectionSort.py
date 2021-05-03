# This sorting takes the minimum from the sub lists and puts it in the front

# Time Complexity - O(n2)

# Space Complexity - O(1)


def sortIt(arr):

    n = len(arr)

    for i in range(n):

        min_ind = i

        # Getting the index of minimum number in the sub array
     
        for j in range(i+1,n):

            if arr[min_ind] > arr[j]:

                min_ind = j
        
        # If the minimum number is not equal to the ith character then we swap the two which 
        # takes it to the front
        if min_ind != i:

            arr[min_ind], arr[i] = arr[i], arr[min_ind]


if __name__ == "__main__":

    arr = [6,7,4,3,12,3,1,9]

    sortIt(arr)

    print(arr)