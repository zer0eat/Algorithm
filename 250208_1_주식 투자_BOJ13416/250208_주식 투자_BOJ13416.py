# 주식 투자_BOJ13416

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())            # 테스트 케이스를 input 받고
for t in range(T):          # 테스트 케이스를 반복해서
    ans = 0                 # 정답을 저장할 변수를 생성하고
    N = int(input())        # 주식을 계산할 일수를 input 받고
    for n in range(N):      # 주식을 계산할 일수를 반복해서
        stock = max(list(map(int, input().split()))) # 가장 수익이 좋은 주식을 저장하고
        if stock > 0:       # 주식으로 수익을 낼 수 있다면
            ans += stock    # 정답에 추가하고
    print(ans)              # N일간 낼 수 있는 최대 수익을 출력한다