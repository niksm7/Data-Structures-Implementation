# Linearly searches for an element in the given array

# Time complexity - O(n) - Linear Time complexity

# Returns the index of the element if present else returns -1

def search(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [3,5,6,7,4,3,2,1]
    x = 2

    print(search(arr,x))

    x = 9

    print(search(arr,x))