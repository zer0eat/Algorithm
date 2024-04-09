# 분산처리_BOJ1009

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트케이스를 input 받고
for t in range(T):                      # 테스트케이스를 반복해서
    a, b = map(int, input().split())    # a 밑과 b 지수를 input 받는다
    ans = a % 10                        # 정답을 저장할 변수를 생성하고
    for i in range(b-1):                # 지수를 반복해서
        ans = (ans*a)%10                # ans에 a를 곱한 후 일의자리수만 저장한다
    if ans == 0:                        # ans가 0이라면
        print(10)                       # 10번 컴퓨터에서 처리하고
    else:                               # 0이 아니라면
        print(ans)                      # ans번 컴퓨터에서 처리한다