# 참외밭_BOJ2477

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
K = int(input())                                            # 1m^2에서 자라는 참외의 개수
node = [list(map(int, input().split())) for n in range(6)]  # 0번인덱스 : 꼭지점의 방향(동:1, 서:2, 남:3, 북:4) / 1번인덱스 : 길이

lst = []                                                    # 밭의 넓이를 저장해줄 리스트
for i in range(len(node)):                                  # 밭의 변을 반복 할때
    lst.append(node[i][1] * node[i-1][1])                   # 사각형의 넓이를 구해 lst에 저장
maxV = 0                                                    # 최대 크기의 사각형을 저장할 변수
idx = 0                                                     # 최대 크기 사각형의 인덱스
for l in range(len(lst)):                                   # 저장된 넓이를 반복하면서
    if lst[l] > maxV:                                       # 최대 넓이보다 큰 넓이가 나오면
        maxV = lst[l]                                       # 최대 넓이에 저장하고
        idx = l                                             # 인덱스를 저장

print((maxV - lst[idx-3]) * K)                              # 최대 넓이에서 3칸 전 넓이가 뺴줘야할 넓이이므로 그 값을 빼주고 1m^2 당 나오는 참외의 수를 곱해  밭 전체에서 나오는 참외의 수를 구한다