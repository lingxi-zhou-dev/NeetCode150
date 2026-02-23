import string

# String modification method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # strip punctuation
        s1 = s.translate(s.maketrans("", "", string.punctuation))

        # strip spaces
        s2 = s1.replace(" ", "").lower()
        print(s1, "\n" ,s2)

        # reverse string
        s3 = s2[::-1]
        
        if s2 == s3:
            return True
        else:
            return False

# Two pointers method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric on the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric on the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True