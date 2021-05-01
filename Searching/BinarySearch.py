# List needs to be sorted

# Searches in a binary way where we keep on comparing the middle element and deciding whether to go for left half or right half

# Time Complexity - O(Log n)

def search(arr,l,r,x):

    while l <= r:

        m = l + (r-l) // 2
        
        # We have done +l here so as to get the middle term while move the left pointer to the right side we are cutting those extra left elements.

        if arr[m] == x:
            return m
        
        if arr[m] > x:
            
            # if the middle element is greater than the required number then we move the right pointer to the number which is left to our middle number

            r = m - 1

        elif arr[m] < x:
            
            # if the middle element is less than the required number then we move the left pointer to the number which is right to our middle number

            l = m + 1
        
    return -1



if __name__ == "__main__":
    arr = [3,4,11,34,54,76]
    x = 54

    print(search(arr,0,len(arr)-1,x))