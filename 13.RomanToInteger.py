class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        # Initialize the result to 0
        result = 0
    
        # Iterate through the string from left to right
        for i in range(len(s)):
            # Get the integer value of the current character
            current_value = roman_to_int.get(s[i], 0)
            # If the current value is less than the value of the next character,
            # subtract it from the result
            if i < len(s) - 1 and current_value < roman_to_int.get(s[i + 1], 0):
                result -= current_value
            # Otherwise, add it to the result
            else:
                result += current_value
    
        return result