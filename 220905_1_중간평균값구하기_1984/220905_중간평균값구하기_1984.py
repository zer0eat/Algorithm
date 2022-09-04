# 중간평균값구하기_1984

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                # 테스트 케이스
for t in range(T):                                              # 테스트 케이스를 반복할 때
    num = list(map(int, input().split()))                       # 숫자열을 리스트로 받음

    for i in range(9):                                          # 오름차순으로 버블정렬
        for j in range(9-i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

    num.pop(0)                                                  # 가장 작은 수 제거
    num.pop()                                                   # 가장 큰 수 제거

    if (sum(num)/len(num)*10) % 10 >= 5:                        # 소수점 첫째짜리가 5 이상이면
        print(f'#{t + 1}', sum(num) // len(num) + 1)            # 반올림하여 1을 더한 정수만 출력
    else:                                                       # 소수점 첫째짜리가 5 이하이면
        print(f'#{t + 1}', sum(num) // len(num))                # 반올림한 후 정수만 출력



