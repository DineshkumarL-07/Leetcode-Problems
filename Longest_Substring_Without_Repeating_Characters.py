# given an string we have to find the longest substring which does not contain any repeating characters

# Input : s = "abcabcbb"
# Output: 3
# Explanation: "abc or bca or cab"

# Input : s = "bbbbb"
# Output: 1

def longest_substring(s):
    character_set = set()
    left = 0
    ans = 0
    for right in range(len(s)):
        while s[right] in character_set:
            character_set.remove(s[left])
            left += 1
        character_set.add(s[right])
        ans = max(ans,right - left + 1)
    return ans

s = input()
print(longest_substring(s))