class Solution:

  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  def twoSum(self, nums, target):
    dic = {}
    for i, v in enumerate(nums):
      if target - v in dic:
        return [dic[target - v], i]
      dic[v] = i


def main():
  sln = Solution()
  result = sln.twoSum([2,7,11,15], 9)
  print(result)

if __name__ == "__main__":
  main()