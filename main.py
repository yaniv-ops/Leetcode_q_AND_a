class Solution:
    """///

    1. Two Sum

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


    ///"""

    def twoSum(self, nums, target):
        list = nums
        list_to_return = []
        result = 1000
        for item in range(len(list)):
            for bacon in range(item+1, len(list)):
                calculate = abs(target - (list[item] + list[bacon]))
                if calculate <= result:
                    result = calculate
                    list_to_return = [item, bacon]
        return list_to_return

    """///

    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.
    
    Follow up: Could you solve it without converting the integer to a string?

    ///"""


    def isPalindrome(self, number: int):

        def flipNum(num: int, number):

            number2 = number
            check_sum =0
            multi = 1
            n = num
            while n >= 1:
                check_sum += number2//n * multi
                number2 = number2%n
                multi *= 10
                n /= 10
            return check_sum

        n = 1
        while number/n >= 10:
            n *= 10
        b = flipNum(n, number)
        if b == number and b/10 > 1:
            return True
        else:
            return False

    '''
                    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
            
            Symbol       Value
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000
            For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
            
            Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
            
            I can be placed before V (5) and X (10) to make 4 and 9. 
            X can be placed before L (50) and C (100) to make 40 and 90. 
            C can be placed before D (500) and M (1000) to make 400 and 900.
            Given a roman numeral, convert it to an integer.

 
    '''
    global total_sum
    total_sum = 0

    def romanToInt(word, sum):

        total_sum = sum
        roman_dict = {'I':1,
                      'IV':4,
                        'V':5,
                      'IX':9,
                        'X':10,
                      'XL':40,
                        'L':50,
                      'XC':90,
                        'C':100,
                      'CD':400,
                        'D':500,
                      'CM':900,
                        'M':1000,
                                }

        worded = word[:2]
        end = word[2:]
        if len(word) == 1:
            total_sum += roman_dict[worded]
            return total_sum

        if worded in roman_dict:
            total_sum += roman_dict[worded]
        else:

            total_sum = total_sum + roman_dict[worded[0]] + roman_dict[worded[1]]

        if len(end) >= 1:
            a = object.romanToInt(end, sum=total_sum)
        else:
            return total_sum
        return a
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
    
    '''

    table = {"[":"]",
            "{":"}",
            "(":")"}

    def check_par_block(self, s: str) -> bool:
        if not s:
            return True
        if s[-1] == self.table[s[0]]:
            if len(s) == 2:
                return True
            result = self.check_par_block(s[1:-1])
            return result
        return False




    def isPar(self, s: str) -> bool:

        num = 0
        for item in range(len(s)-1):
            if s[item] in self.table.values() and s[item +1] in self.table.keys():
                into = s[num:item +1]
                result = self.check_par_block(into)
                share = self.isPar(s[item +1: len(s)])
                num = item +1
                if result == share:
                    return share
                else:
                    return False
        result = self.check_par_block(s)
        return result


'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



'''

global max
max = 0

def maxArea(height) -> int:

    while height:
        for item in range(len(height)-1):
            if height[item] <= height[len(height) -1]:
                result = int(height[item] * len(height[item:len(height) -1]))
            else:
                result = int(height[len(height) -1 ] * len(height[item:len(height) -1]))
            global max
            if result > max:
                max = result
        height.pop()
        maxArea(height)
    return max

number_max = maxArea([1,8,6,2,5,4,8,3,7])
print(number_max)

'''



'''



def findLucky(arr):
    unrep = list(set(arr))
    unrep.sort(reverse=True)
    for val in unrep:
        if val == arr.count(val):
            return val
    return -1
