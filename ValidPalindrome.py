import string
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

        