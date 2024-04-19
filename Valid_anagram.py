# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

def is_anagram(s,t):
    if len(s) != len(t):
        return False
    hashMap1, hashMap2 = {}, {}
    for i in range(len(s)):
        hashMap1[s[i]] = 1 + hashMap1.get(s[i],0)
        hashMap2[t[i]] = 1 + hashMap2.get(t[i],0)
    
    return hashMap1 == hashMap2

s = "anagram"
t = "nagaram"
print(is_anagram(s,t))
