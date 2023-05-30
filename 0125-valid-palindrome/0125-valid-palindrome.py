class Solution(object):
    def isPalindrome(self, s):
        i = 0 ; j = len(s)-1
        while i<=j:
        
            while not (97 <= ord(s[i]) <= 122) and not (65 <= ord(s[i]) <= 90) and not (48 <= ord(s[i]) <= 57):
                if i + 1 >j:
                    break
                i += 1
            while not(97 <= ord(s[j]) <= 122) and not(65 <= ord(s[j]) <= 90) and not (48 <= ord(s[j]) <= 57):
                if i > j-1:
                    break
                j -= 1
            if 65 <= ord(s[i]) <= 90:
                cur = chr(ord(s[i])+32)
            else:
                cur = s[i]
            if 65 <= ord(s[j]) <= 90:
                cur2 = chr(ord(s[j])+32)
            else:
                cur2 = s[j]
            if cur != cur2:
                return False
            i += 1; j-=1
        return True
                
                
        