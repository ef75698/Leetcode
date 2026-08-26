class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = []
        for c in s: 
            if c.isalnum():
                x.append(c.lower())
        return x == x[::-1]