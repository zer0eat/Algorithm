# 카드 게임 (Easy)_BOJ32141

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, H = map(int, input().split())    # 카드의 수와 체력을 input받고
D = list(map(int, input().split())) # 카드 리스트를 반복해서
ans = 0                             # 사용한 카드의 수를 저장할 변수를 생성하고
for d in D:                         # 카드 리스트를 반복해서
    H -= d                          # 체력에서 공격카드 만큼 빼고
    ans += 1                        # 사용한 카드 수를 출력한다
    if H <= 0:                      # 체력이 없다면
        print(ans)                  # 사용한 카드 수를 출력하고
        break                       # 종료한다
else:                               # 체력이 남아 있다면
    print(-1)                       # -1을 출력한다