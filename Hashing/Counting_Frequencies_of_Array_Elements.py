class Solution:
    def countFrequencies(self, nums):
        arr = set(nums)
        arr = list(arr)
        def help(arr):
            res = []
            for i in arr:
                count = 0
                v = []
                v.append(i)
                for j in nums:
                    if i == j:
                        count +=1
                v.append(count)
                res.append(v)
            return res
        a =help(arr)
        return a
if __name__ == "__main__":
    s = Solution()
    r = s.countFrequencies([1, 2, 2, 1, 3])
    print(r)
            