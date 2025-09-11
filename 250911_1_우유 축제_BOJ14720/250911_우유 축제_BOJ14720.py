# 우유 축제_BOJ14720

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 가게의 수를 input받고
market = list(map(int, input().split()))    # 가게의 정보를 리스트로 input받고
ans, tmp = 0, 0             # 마신 우유의 수와 현재 마시고 싶은 우유를 저장할 변수를 생성하고
for n in range(N):          # 가게를 반복해서
    if market[n] == tmp:    # 현재 마시고 싶은 우유를 판다면
        ans += 1            # 마신 우유의 수를 1 더해주고
        tmp = (tmp+1)%3     # 다음 마시고 싶은 우유로 변경한다
print(ans)                  # 총 마신 우유의 수를 출력한다