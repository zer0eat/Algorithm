# 종이자르기_BOJ2628

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
L, H = map(int,input().split())                                         # L = 가로의 길이 / H = 세로의 길이
cut = int(input())                                                      # 자를 점선의 개수
cut_info = [list(map(int, input().split())) for _ in range(cut)]        # 0번인덱스 : 0 = 가로, 1 = 세로로 자름 / 1번인덱스: 점선 번호

# 종이 자르기
width = [0, L]                                                          # 가로의 범위를 리스트로 저장
vertical = [0, H]                                                       # 세로의 범위를 리스트로 저장

for c in cut_info:                                                      # 잘린 정보를 반복할 때
    if c[0] == 0:                                                       # 가로로 잘랐으면
        vertical.append(c[1])                                           # 잘린 위치를 세로의 범위에 저장
    elif c[0] == 1:                                                     # 세로로 잘랐다면
        width.append(c[1])                                              # 잘린 위치를 가로의 범위에 저장

width.sort(reverse=True)                                                # 내림차순으로 정렬
vertical.sort(reverse=True)                                             # 내림차순으로 정렬

maxW = 0                                                                # 가로의 길이 중 가장 긴 값을 구하기 위한 변수
for w in range(len(width)-1):                                           # 잘린 위치를 반복할 때
    if width[w] - width[w+1] > maxW:                                    # 맨 뒤에서 부터 maxW보다 긴 가로의 길이가 나오면
        maxW = width[w] - width[w+1]                                    # maxW를 바꿔준다
maxV = 0                                                                # 세로의 길이 중 가장 긴 값을 구하기 위한 변수
for v in range(len(vertical)-1):                                        # 잘린 위치를 반복할 때
    if vertical[v] - vertical[v+1] > maxV:                              # 맨 뒤에서 부터 maxV보다 긴 가로의 길이가 나오면
        maxV = vertical[v] - vertical[v+1]                              # maxV를 바꿔준다

print(maxW*maxV)

