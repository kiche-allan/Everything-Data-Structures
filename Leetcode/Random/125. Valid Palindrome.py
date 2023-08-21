class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #remove non-alphanumeric characters using regex
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]