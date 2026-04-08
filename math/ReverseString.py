class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        
        sign = -1 if x < 0 else 1
        a = abs(x)
        
        while a > 0:
            digit = a % 10
            a = a // 10
            
            # 🔥 Overflow check
            if result > (2**31 - 1) // 10:
                return 0
            
            result = result * 10 + digit
        
        return sign * result