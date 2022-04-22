# 재귀구조로 뒤집기

from typing import List
 
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = None
 
def reverse_list(head):
  def reverse(node, prev=None):
    if not node:
      return prev
    next, node.next = node.next, prev
    return reverse(next, node)
    
  return reverse(head)
  
  

  # 반복 구조로 뒤집기
  
def reverse_list(head):
  node, prev = head, None
 
  while node:
    next, node.next = node.next, prev
    prev, node = node, next
 
  return prev
