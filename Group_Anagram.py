# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def group_anagram(strs):

    res = defaultdict(list)
    for word in strs:
        pattern = [0] * 26
        for letter in word:
            pattern[ord(letter) - ord('a')] += 1
        res[tuple(pattern)].append(word)
    return res.values()


strs = list(map(str,input().split()))
print(group_anagram(strs))