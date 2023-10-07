# 창문 닫기_BOJ13909

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 창문의 수를 input 받고
ans = 0                     # 열려있는 창문의 수를 저장할 변수를 생성하고
for i in range(1, N+1):     # 1부터 N까지 반복해서
    if i**2 <= N:           # i의 제곱수라 닫혔다가 다시 열리는 상황의 경우 N보다 작다면
        ans += 1            # 해당 창문은 열려있으므로 1을 추가하고
    else:                   # N보다 크면 N이상의 창문이므로
        break               # for문을 break한 후
print(ans)                  # 열려있는 창문의 수를 출력한다
