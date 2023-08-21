# If we were to use the approach of reversing the integer by first transforming it into a string, we could use the following code:

class Solution:
    def reverse(self, x: int) -> int:
        #convert the interger to as tring and check if its negative
        is_negative = False 
        if x < 0:
            is_negative = True 
            x *= -1
        str_x = str(x)
        # reversethe string
        reversed_str = str_x[::-1]
        
        #convert the reversed string back to an interger
        reversed_int = int(reversed_str)
        #if the original interger was negative, make the reversed interger negative
        if is_negative:
            reversed_int *= -1
        #check if the reversed interger is within the 32-bit integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int
    