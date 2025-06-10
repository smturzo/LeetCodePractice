def merge(nums1, m, nums2, n):
    # Initialize pointers
    p1, p2, p = m - 1, n - 1, m + n - 1

    # Merge arrays starting from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
            print('p1 and p2 >=0, p1 is',p1)
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
            print('else of p1 and p2 >=0, p2 is',p2)
        p -= 1
        print(p)

    # If nums2 still has elements, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
        print('p2 >=0, p is',p)

nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nproblems = 3
attempts = 10
for i in range(nproblems * attempts):
    print(i // attempts, i % attempts, i)
    #print(i//10, i %10, i)