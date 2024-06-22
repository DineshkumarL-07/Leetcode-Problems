# given an integer array and target we have to find which two index sum is equal to target

# Input : nums = [2,7,11,15], target = 9
# Output : [0,1]

# Input : nums = [3,2,4], target = 6
# Output: [1,2]

def two_sum(nums,target):
    hashMap = {}
    for ind,val in enumerate(nums):
        diff = target - val
        if diff in hashMap:
            return [hashMap[diff],ind]
        hashMap[val] = ind


nums = list(map(int,input().split()))
target = int(input())
print(two_sum(nums,target))