# 창고다각형_BJ2304

# input.txt 열기
import sys
sys.stdin = open('input2.txt')

# input 받기
N = int(input())                                                        # N = 기둥의 개수
All_LH = []
for n in range(N):                                                      # 기둥의 개수만큼 반복할 때
    LH = list(map(int, input().split()))                                # 0번 인덱스 = 기둥의 왼쪽 좌표 / 1번 인덱스 = 기둥의 높이
    All_LH.append(LH)                                                   # 기둥 하나하나를 All_LH 리스트에 저장
# print(All_LH)

# 버블 솔트
for i in range(N - 1):                                                  # 버블 솔트를 해서
    for j in range(N - i -1):
        if All_LH[j][0] > All_LH[j + 1][0]:                             # x축의 순서대로 정렬한다
            All_LH[j], All_LH[j + 1] = All_LH[j + 1], All_LH[j]
# print(All_LH)

# 가장 높은 기둥 구하기
high_h = [0, [0, 0]]                                                    # 0번 인덱스는 All_LH의 기둥 인덱스 / 1번 인덱스는 기둥의 x,y 좌표를 리스트로 저장
for h in range(len(All_LH)):                                            # 모든 기둥의 개수만큼 반복할 때
    if All_LH[h][1] > high_h[1][1]:                                     # 새롭게 높은 기둥이 나오면 리스트를 초기화하고
        high_h = []
        high_h.append(h)                                                # 기둥의 인덱스와
        high_h.append(All_LH[h])                                        # 기둥의 x,y 좌표를 리스트로 append
    elif All_LH[h][1] == high_h[1][1]:                                  # 만약 같은 기둥의 높이가 나왔다면
        high_h.append(h)                                                # 리스트를 초기화 하지 않고 기둥의 인덱스와
        high_h.append(All_LH[h])                                        # 기둥의 x,y 좌표를 리스트로 append
# print(high_h)

uuu = 0                                                                 # 창고의 넓이의 합을 저장할 변수

# 가장 높은 기둥의 넓이
if len(high_h) == 2:                                                    # 가장 높은 기둥을 저장해둔 리스트의 길이가 2면 가장 높은 기둥이 한개이므로
    uuu += 1 * high_h[1][1]                                             # uuu에 가로가 1이고 세로가 기둥의 높이인 사각형의 넓이를 구해서 더한다
elif len(high_h) != 2:                                                  # 만약 저장해둔 리스트의 길이가 2가 아니라면 가장 높은 기둥이 한개 이상이므로
    uuu += (high_h[-1][0] - high_h[1][0] + 1) * high_h[1][1]            # 가로의 길이(마지막 기둥의 x좌표 - 첫번째 기둥의 x좌표 +1)와 기둥의 높이를 곱해 넓이를 구한다
# print(uuu)

#처음 기둥 부터 다음 높이의 기둥까지 넓이를 더하며 가장 높은 기둥까지
ooo = All_LH[0]                                                         # 맨 앞 기둥의 x,y 좌표를 ooo에 저장
for l in range(high_h[0] + 1):                                          # 가장 높은 기둥 중 첫번째 기둥까지 반복할 때
    if ooo[1] < All_LH[l][1]:                                           # 첫번째 기둥 보다 높은 기둥이 나오면
        uuu += (All_LH[l][0] - ooo[0]) * ooo[1]                         # (다음기둥의 x좌표 - 처음기둥의 x좌표) * 처음 기둥의 y 좌표로 넓이를 구해 uuu에 더한다
        ooo = All_LH[l]                                                 # ooo를 다음 높이의 기둥으로 교체한다
# print(uuu)

# 맨 뒤에서 다음높이의 기둥까지 넓이를 더하며 가장 높은 기둥까지
qqq = All_LH[-1]                                                        # 맨 뒤 기둥의 x,y 좌표를 qqq에 저장
for p in range(N-1, high_h[-2] - 1, -1):                                # 가장 높은 기둥 중 마지막 기둥까지 뒤에서 앞으로 반복할 때
    if qqq[1] < All_LH[p][1]:                                           # 마지막 기둥 보다 높은 기둥이 나오면
        uuu += (qqq[0] - All_LH[p][0]) * qqq[1]                         # (처음기둥의 x좌표 - 다음기둥의 x좌표) * 처음 기둥의 y 좌표로 넓이를 구해 uuu에 더한다
        qqq = All_LH[p]                                                 # qqq를 다음 높이의 기둥으로 교체한다

print(uuu)                                                              # 전체 넓이를 출력한다