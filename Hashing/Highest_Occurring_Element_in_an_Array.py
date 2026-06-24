class Solution:
    def mostFrequentElement(self, nums):
        arr = set(nums)
        arr = list(arr)
        def help(arr):
            res = []
            for i in arr:
                count = 0
                v =[]
                v.append(i)
                for j in nums:
                    if i == j:
                        count +=1
                v.append(count)
                res.append(v)
            print(res)
            max_second = max(i[1] for i in res)
            ans = float('inf')
            for a, b in res:
                if b == max_second:
                    ans = min(ans, a)
            print(ans)
            return ans
        return help(arr)
s = Solution()
r = s.mostFrequentElement([1,2,2,3,3,3])
print(r)
                
            