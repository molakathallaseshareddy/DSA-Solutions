#Solution 1
class Solution:
    def selectionSort(self, nums:list):
        result = sorted(nums)
        return result
s = Solution()
res =s.selectionSort([3,5,1,2,4])
print(res)

#Solution 2
class Solution:
    def selectionSort(self, nums:list):
        nums.sort()
        return nums
s = Solution()
res =s.selectionSort([3,5,1,2,4])
print(res)

#Solution 3
class Solution:
    def selectionSort(self, nums):
        result = []
        def help(nums):
            a = nums[0]
            for i in nums:
                if a>i:
                    a = i
                    continue
            result.append(a)
            nums.remove(a)
            if len(nums) == 0:
                return
            help(nums)
        help(nums)
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.selectionSort([4,5,2,3,1]))

#Solution 4
class Solution:
    def selectionSort(self, nums):
        result =[]
        def help():
            if len(nums) == 0:
                return
            num = nums[0]
            for i in nums:
                if num > i:
                    num = i
            result.append(num)
            nums.remove(num)
            return help()
        help()
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.selectionSort([2,4,1,3,6,5]))
            
#Solution 5 reverse selection sort
class Solution:
    def selectionSort(self, nums):
        result =[]
        def help():
            if len(nums) == 0:
                return
            num = nums[0]
            for i in nums:
                if num < i:
                    num = i
            result.append(num)
            nums.remove(num)
            return help()
        help()
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.selectionSort([2,4,1,3,6,5]))
    
 
# Selection Sort Implementation   
li = [5, 1, 43, 54, 23, 67, 87, 3]
for i in range(len(li)):
  min_index = i
  for j in range(i+1, len(li)):
    if li[min_index] > li[j]:
      min_index = j
  li[i], li[min_index] = li[min_index], li[i]
print(li)