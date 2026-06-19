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
        def helper(left, right):
            if left >= right:
                return

            arr[left], arr[right] = arr[right], arr[left]

            helper(left + 1, right - 1)

        helper(0, n - 1)