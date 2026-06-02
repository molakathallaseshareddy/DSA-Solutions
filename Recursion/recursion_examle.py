def solution(count):
    if count == 5:
        return
    count +=1
    print(count)
    solution(count)
if __name__ == '__main__':
    solution(0)