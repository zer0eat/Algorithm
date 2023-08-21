# 수들의 합5_BOJ2018

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 자연수를 input 받고
ans = 0                         # 정답을 저장할 변수를 생성한다
for i in range(1, N+1):         # 1부터 N까지 반복해서
    tmp = 0                     # N이랑 비교할 변수를 생성하고
    while 1:                    # break가 나올때까지 반복해서
        tmp += i                # tmp에 i를 더하고
        if tmp == N:            # tmp가 N과 같다면
            ans += 1            # ans에 1을 저장하고
            break               # while문을 break 한다
        elif tmp > N:           # tmp가 N보다 커졌다면
            break               # while문을 break 한다
        i += 1                  # i에 1을 추가한다
print(ans)                      # 연속된 자연수의 합으로 나타내는 가지수를 출력한다