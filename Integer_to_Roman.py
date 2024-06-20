# given an integer number we have to convert into roman number

# Input : 110
# Output : CX

hashMap = {
    1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9 : "IX",
    5 : "V",
    4 : "IV",
    1 : "I"
}

num = int(input())
ans = ""
for number, chara in hashMap.items():
    if num // number:
        count = num // number
        ans += (chara*count)
        num = num % number
print(ans)