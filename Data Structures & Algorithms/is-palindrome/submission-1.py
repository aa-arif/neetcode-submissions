class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr, right_ptr = 0, len(s) - 1
        while (left_ptr < right_ptr): 
            while left_ptr < right_ptr and s[left_ptr].isalnum() == False: 
                left_ptr += 1
            while left_ptr < right_ptr and s[right_ptr].isalnum() == False: 
                right_ptr -= 1
            if s[left_ptr].lower() != s[right_ptr].lower(): 
                return False 
            left_ptr += 1
            right_ptr -= 1
        return True
        