"""Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Leetcode: https://leetcode.com/problems/product-of-array-except-self/

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""


# T.C - O(n)
# S.C - O(n)
# def product_except_current(arr):
#     temp = 1
#     for val in arr:
#         temp *= val
#     prod = [0] * len(arr)
#     for i in range(len(arr)):
#         prod[i] = temp // arr[i]
#     return prod

# T.C - O(n)
# S.C - O(n)
# def product_except_current(arr):
#     n = len(arr)
#     left = [0] * n
#     right = [0] * n
#     left[0] = 1
#     right[-1] = 1
#     prod = [0] * n
#     for i in range(1, n):
#         left[i] = left[i - 1] * arr[i - 1]
#     for j in range(n - 2, -1, -1):
#         right[j] = right[j + 1] * arr[j + 1]
#     for k in range(n):
#         prod[k] = left[k] * right[k]
#     return prod

# T.C - O(n)
# S.C - O(1) Not counting the output array
def product_except_current(arr):
    n = len(arr)
    prod = [1] * n
    temp = 1
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]
    temp = 1
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]
    return prod


if __name__ == "__main__":
    print(product_except_current([1, 2, 3, 4, 5]))
    print(product_except_current([3, 2, 1]))
