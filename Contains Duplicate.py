# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Code

def contains_duplicate(nums):
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))

