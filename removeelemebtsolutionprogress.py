class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #nums is an list of integers, val is an integer
        #move all nums equal to val are moved behind the kth position
        k = 0
        for i in range(0, len(nums) - 1, 1):
            if nums[i] != val:
                #get the comparison working
             #how to move an array index
             #k is the number of elements in nums not equal to k
                #first k elements of the array must not be equal to val
                #move all elements equal to val behind the elements that arent equal to val
                #or try removing them
              k += 1
              nums.pop()
            



        
        return k
           # print(nums[0])



   # removeElement([12345])
