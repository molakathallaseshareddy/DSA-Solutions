# def solution(num,count):
#     if num == count:
#         return
#     print("Python + AWS")
#     count += 1
#     solution(num, count)
# if __name__ == "__main__":
#     solution(3, 0)


def solution(n):
    if n==0:
        return
    print("Python + AWS")
    solution(n-1)
if __name__ == "__main__":
    solution(3)