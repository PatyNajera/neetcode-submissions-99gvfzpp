class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for l in s:
          if l.isalnum():
              n+=l.lower()

        return n[::-1]==n