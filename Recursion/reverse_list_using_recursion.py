#First Solution
class Solution:
    def reverse(self, arr: list, n: int) -> None:
        if n==1:
            return [arr[n-1]]
        return [arr[n-1]]+self.reverse(arr, n-1)
if __name__ == "__main__":
    s= Solution()
    print(s.reverse([1,2,3,4,5],5))


#Second Solution
class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def help(i, j):
            if i > j:
                return
            arr[i], arr[j] = arr[j], arr[i]
            help(i+1, j-1)
        help(0, n-1)