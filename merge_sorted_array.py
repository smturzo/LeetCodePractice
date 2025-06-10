def merge_sorted_array(nums1, m, nums2, n):
    """
    Purpose of fuction: This function merges two sorted arrays, nums1 and nums2, into the first array, nums1.
        Note: nums1 initially has a length of m valid elements, 
              followed by enough empty spaces (0s or placeholder) 
              to accommodate elements from nums2.
        Note: nums2 has exactly n valid elements.
    Parameters:
    nums1: List with a total size of m + n, containing m meaningful numbers, followed by placeholders.
    m: Number of valid elements in nums1.
    nums2: List with exactly n valid elements.
    n: Number of valid elements in nums2.
    """
    # Initialize pointers
    """
    p1, p2, p: Points to the last valid element in nums1, nums2 and combined array respectively.
    """
    p1, p2, p = m - 1, n - 1, m + n - 1
    # Merge arrays starting from the end
    while p1 >= 0 and p2 >= 0:

        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    # If nums2 still has elements, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# Inputs
nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3

merge_sorted_array(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
