def is_palindrome(input_string):
        new_string = ""
        reverse_string = ""
        for letter in input_string:
            if letter.lower() != "":
                new_string = "{}{}".format(new_string, letter).strip()
                reverse_string = "{}{}".format(letter, reverse_string).strip()
        if new_string.lower().strip() == reverse_string.lower().strip():
           return True
        return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True