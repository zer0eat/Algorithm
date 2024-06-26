# ZOAC 4_BOJ23971

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
H, W, N, M = map(int, input().split())  # H 세로의 길이 / W 가로의 길이 / N 세로로 떨어질 칸 / M 가로로 떨어질 칸을 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성하고
for n in range(0, H, 1+N):              # 세로를 N칸씩 띄워가며 반복하고
    for m in range(0, W, 1+M):          # 가로를 M칸씩 띄워가며 반복하고
        ans += 1                        # 사람을 추가한다
print(ans)                              # 강의실이 수용할 수 있는 최대 인원 수를 출력한다