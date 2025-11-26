"""
The problem: 


From --> https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
 

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


# The following Docstrings are mine:
#
#
"""
Note: 
        In two for loop that one of them is nested loop, if we put a break into the nested loop, the nested loop will be stoped 
    and the outer loop still continue working.

enumerate() Function:
    * The /enumerate()/ function takes a collection (e.g. a tuple, list or whatever) and returns it as an enumerate object.
    * The /enumerate()/ function adds a counter as the key of the enumerate object.
    
    Example:
        x = ('apple', 'banana', 'cherry')
        y = enumerate(x)
        print(list(y))
        
        output:
            [(0, 'apple), (1, 'banana'), (2, 'cherry')]
            
    Point:
        If you don't convert it into a list, it will return a non-unhuman-readable object.
"""

# My code
# I don't delete it because it helps me to find out why I was close to solve the problem but couldn't.
"""
def move_on (arr, target):
    index = 0
    result = []
    for i in arr:
        jindex = index + 1
        for j in arr[jindex : ]:
            sum_value = i + j
            if sum_value == target:
                return result.extend((index, jindex))
            
            index += 1
            break
"""

# Point: I fully understand following code. I told chat-GPT to correct me.
def move_on(arr, target):
    for i_index, i_value in enumerate(arr):
        for j_index in range(i_index + 1, len(arr)):
            j_value = arr[j_index]
            
            if i_value + j_value == target:
                return [i_index, j_index]

nums = [2,7,11,15] 
target = 26

print(move_on(nums, target))

# ToDo: Still have work if you want to improve it. You need to find another way that the time complexity is less than O(n^2).