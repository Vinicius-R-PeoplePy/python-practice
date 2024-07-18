'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If it is, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 is not None or l2 is not None:
            # Get the values from the current nodes, if they exist
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum of the values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit
            
            # Move to the next nodes in the lists
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's any carry left after the final addition, create a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # The result list starts after the dummy node
        return dummy.next

# Example usage:
def create_linked_list(numbers):
    dummy = ListNode(0)
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result

# Test cases
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [0]

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
