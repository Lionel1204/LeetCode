# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """
  def addTwoNumbers(self, l1, l2):
    resultPtr = ListNode(0)
    resultList = resultPtr
    pl1 = l1
    pl2 = l2
    carry = 0

    while True:
      if None is pl1 and None is not pl2:
        result = pl2.val + carry
        pl2 = pl2.next
      elif None is pl2 and None is not pl1:
        result = pl1.val + carry
        pl1 = pl1.next
      elif None is pl1 and None is pl2 and carry > 0:
        result = carry
      else:
        result = pl1.val + pl2.val + carry
        pl1 = pl1.next
        pl2 = pl2.next

      carry = 0
      if result >= 10:
        resultPtr.val = result % 10
        carry = 1
      else:
        resultPtr.val = result

      if (None is pl1 and None is pl2) and carry == 0:
        resultPtr.next = None
        break
      resultPtr.next = ListNode(0)
      resultPtr = resultPtr.next

    return resultList

def main():
  sln = Solution()
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)


  result = sln.addTwoNumbers(l1, l2)
  print(result)

if __name__ == "__main__":
  main()