# 생일선물_BOJ12892

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, D = map(int, input().split())                # N 친구의수 / D 미안함을 느끼는 가격차이

gift = []                                       # 선물을 저장할 리스트 생성
for _ in range(N):                              # 친구의 수 만큼 반복해서
    gift.append(list(map(int, input().split())))    # A에 [선물가격, 선물만족도]를 input 받고
gift.sort()                                     # 선물 가격에 따라 오름차순으로 정렬

keyboard = 0                                    # 최고 만족도를 저장할 변수 생성
s = 0                                           # 시작점의 포인터 생성
e = 0                                           # 끝 점의 포인터 생성
custom = 0                                      # 임시 만족도를 저장할 변수 생성
for e in range(N):                              # 친구의 수만 큼 반복해서
    custom += gift[e][1]                        # 임시만족도 변수에 끝점의 만족도를 더하고
    while gift[e][0] - gift[s][0] >= D:         # 끝점의 만족도와 시작점의 만족도의 차가 D보다 작아질때까지 반복해서
        custom -= gift[s][1]                    # D보다 클 경우에 시작점의 만족도를 뺀 후
        s += 1                                  # 시작점을 오른쪽으로 한 칸 이동한다
    if keyboard < custom:                       # D보다 작아진 경우에 최고만족도와 임시만족도를 비교해서 임시만족도가 더 크면
        keyboard = custom                       # 최고만족도를 임시만족도로 바꿔 저장한다

print(keyboard)                                 # 모든 선물을 살펴보았다면 최고만족도를 출력한다