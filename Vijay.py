""" Q - To find longest palindromic substring """

def longestpalindrome(s):
    longest = ""
    for i in range(len(s)):
        temp = ""
        for j in range(i,len(s)):
            substring = ""
            temp += s[j]
            if temp == temp [::-1]:
                substring += temp
            if len(substring) > len(longest):
                longest = substring
    return longest
print(longestpalindrome("babad"))




""" Q - Next prime number """
def nextprime(num):
    number = num + 1
    while number > 0:
        factors = 0
        for i in range(1,number+1):
            if number % i == 0:
                factors += 1
        if factors == 2:
            return number
        else:
            number += 1
num = nextprime(7)
print(num)



""" Q - Find length of Longest Substring Without Repeating Characters """

def longestsubstring(s):
    longest = ""
    for i in range(len(s)):
        temp = ""
        for j in range(i,len(s)):
            if s[j] not in temp:
                temp += s[j]
        if len(temp) > len(longest):
            longest = temp
    return len(longest)
length_substring = longestsubstring("abcabcbb")
print(length_substring)



""" Q - Anagram check """
def Anagram_check(s1,s2):
    str1 = sorted(s1)
    str2 = sorted(s2)
    if str1 == str2:
        return True
    else:
        return False
anagram = Anagram_check("iamlordvoldemort","tommarvoloriddle")
print(anagram)


""" Q - Armstrong number """
def Armstrong(n):
    original = n
    length = len(str(n))
    result = 0
    while n > 0:
        last_digit = n % 10
        result += last_digit ** length
        n //= 10
    if result == original:
        return True
    else:
        return False
checking = Armstrong(153)
print(checking)


""" Q - Flatten a Nested List """
def Flatten_nestedlist(nested_list):
    result = []
    for i in nested_list:
        result.extend(i)
    return result
nested_list = [[1,2,3],[4,5],[6,7,8,9]]
result = Flatten_nestedlist(nested_list)
print(result)



""" Q - Sum of individual elements of list """
def Sum_of_each_element(nums):
    Total = 0
    for i in nums:
        while i > 0:
            digit = i % 10
            Total += digit
            i //= 10
    return Total
nums = [12,13,19]
result = Sum_of_each_element(nums)
print(result)