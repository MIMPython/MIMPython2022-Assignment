def isPalindrome(num): # Function to check if a number is a palindrome
    rev_num = int(str(num)[::-1])
    if num == rev_num:
        return True
    else:
        return False

def main():
    count = 0
    for i in range(100000):
        if isPalindrome(i**2):
            count += 1
    print (count)
    
if __name__ == "__main__":
    main()