def solution(num,count):
    if num == count:
        return
    print("Python + AWS")
    count += 1
    solution(num, count)
if __name__ == "__main__":
    solution(3, 0)