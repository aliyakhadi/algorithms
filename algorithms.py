class Solution:
  def countPairs(self, nums: List[int], target: int) -> int:
    return sum(nums[i] + nums[j] < target
               for i in range(len(nums))
               for j in range(i + 1, len(nums)))
    #unfortunately, that is not a solving of a Week Task which is Prime Sum Problem
    # you can find it there : https://www.interviewbit.com/problems/prime-sum/ 
    #
