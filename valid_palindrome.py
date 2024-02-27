def isPalindrome(s: str) -> bool:
    lptr = 0
    rptr = len(s) - 1
    while lptr < rptr:
        if s[lptr].isalnum() and s[rptr].isalnum():
            if s[lptr].lower() == s[rptr].lower():
                lptr += 1
                rptr -=1
            else:
                return False
        elif s[lptr].isalnum():
            rptr -= 1
        elif s[rptr].isalnum():
            lptr += 1
        else:
            rptr -= 1
            lptr += 1
    return True

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
s = "0P"
print(isPalindrome(s))