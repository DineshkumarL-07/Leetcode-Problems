# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


digits = {
    "2" : "abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"
}
combinations = []
def backtrack(ind,str):
    if len(str) == len(digit):
        combinations.append(str)
        return 
    for letter in digits[digit[ind]]:
        backtrack(ind+1,str+letter)

digit = input("Enter the Number: ")
backtrack(0,"")
print(*combinations)