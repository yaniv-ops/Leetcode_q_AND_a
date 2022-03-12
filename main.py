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
        a = romanToInt(end, sum=total_sum)
    else:
        return total_sum
    return a


a = romanToInt('XXIX', 0)



