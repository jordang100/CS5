#
# CodingBat Problems
# Name: Lawrence Mao
# Date: 10-28-17
#

def count_evens(nums):
  result = 0
  for c in nums:
    if c % 2 == 0:
      result += 1
  return result

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  sum = 0
  for c in nums:
    sum += c
  return (sum - min(nums) - max(nums)) / (len(nums)-2) 

def sum13(nums):
  if len(nums) == 0:
    return 0
  for c in range(0, len(nums)):
    if nums[c] == 13:
      nums[c] = 0
      if c+1 < len(nums): 
        nums[c+1] = 0
  return sum(nums)

def sum67(nums):
  for c in range(0, len(nums)):
    if nums[c] == 6:
      nums[c] = 0
      for j in range(c+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)

def has22(nums):
  for c in range(0,len(nums) - 1):
    if nums[c] == 2 and nums[c+1] == 2:
      return True
  return False

def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

def count_hi(str):
  result = 0
  for c in range(len(str)-1):
    if str[c:c+2] == 'hi':
      result += 1
  return result

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      dog += 1
    if str[i:i+3] == 'cat':
      cat += 1
  return cat == dog

def count_code(str):
  count = 0
  for c in range(len(str)-3):
    if str[c:c+2] == 'co' and str[c+3] == 'e':
      count += 1
  return count

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):] 

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False