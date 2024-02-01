# 작은벌점_BOJ16498

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split())                     # 플레이어의 카드 숫자를 input 받고
card1 = list(map(int, input().split()))                 # 1플레이어의 카드를 input 받고
card2 = list(map(int, input().split()))                 # 2플레이어의 카드를 input 받고
card3 = list(map(int, input().split()))                 # 3플레이어의 카드를 input 받는다
ans = 10000000000                                       # 정답을 저장할 변수를 생성하고
for c1 in card1:                                        # 1플레이어 카드를 반복하고
    for c2 in card2:                                    # 2플레이어 카드를 반복해서
        if abs(max(c1,c2) - min(c1,c2)) >= ans:         # 1,2번 카드의 벌점이 현재 저장된 값보다 크다면
            continue                                    # 3 플레이어 카드를 안봐도 최소가 될수 없으므로 continue한다
        for c3 in card3:                                # 3플레이어 카드를 반복해서
            tmp = abs(max(c1,c2,c3) - min(c1,c2,c3))    # 벌점을 구하고
            ans = min(tmp, ans)                         # tmp 벌점과 ans 벌점 중 작은 값을 저장한다
print(ans)                                              # 세 플레이어가 만들 수 있는 가장 작은 벌점을 출력한다