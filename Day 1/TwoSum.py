"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

GFG: https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/
"""


# T.C - O(n^2)
# S.C - O(1)
# def twoSum(arr, k):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == k:
#                 return True
#     return False

# T.C - O(n)
# S.C - O(n)
def two_sum(arr, k):
    prev = set()
    for val in arr:
        if k - val in prev:
            return True
        prev.add(val)
    return False


if __name__ == "__main__":
    print(two_sum([10, 15, 3, 7], 17))
