class Solution:
    def PrimeNo(value):
        if value <=1:
            return "Not Prime Value"
        for i in range(2, value):
            if value % i == 0:
                return "Not Prime Number"
        return "Prime Number"
if __name__ == "__main__":
    f = Solution.PrimeNo(4)
    print(f)