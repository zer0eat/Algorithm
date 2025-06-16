# 3000번 버스_BOJ9546

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
k = int(input())            # 버스의 수를 input받고
for b in range(k):          # 버스의 수를 반복해서
    n = int(input())        # 정류장의 수를 반복해서
    ans = 0                 # 정답을 저장할 변수를 생성하고
    for _ in range(n):      # 정류장의 수를 반복해서
        ans = ans*2 +1      # 승객을 구하고
    print(ans)              # 처음 승객의 수를 출력한다