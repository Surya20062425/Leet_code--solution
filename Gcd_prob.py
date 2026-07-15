import math

# Imported math package to perform  the GCD operation
class Solution:


  # created a cllass solution
    def gcdOfStrings(self, str1: str, str2: str) -> str:


      # created a function with  parameters str1,str2 
        # Step 1: Check if a common divisor string even exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: The answer is the prefix of length = GCD of lengths
        gcd_length = math.gcd(len(str1), len(str2))
        
        return str1[:gcd_length]
