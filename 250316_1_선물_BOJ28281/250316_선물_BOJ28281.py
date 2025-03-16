# 선물_BOJ28281

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, X = map(int, input().split())        # 남은 생일과 사야하는 양말의 수를 input 받고
socks = list(map(int, input().split())) # 양말의 가격을 리스트로 input 받는다
ans = 1000000000                        # 정답을 저장할 변수를 생성하고
for n in range(N-1):                    # 남은 생일 반복해서
    ans = min(ans, socks[n]+socks[n+1]) # 2일 연속 양말을 살때 가장 낮은 가격을 구해서
print(ans*X)                            # 가장 싸게 살 수 있는 금액을 출력한다