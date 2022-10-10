# 마인크래프트_BOJ18111

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
row, col, inventory = map(int, sys.stdin.readline().split())    # row 땅 행의길이 / col 땅 열의길이 / inventory 가지고 있는 블록의수
rc = row * col                                                  # 땅고르기 작업을 할 총 칸수

arr = list(map(int, sys.stdin.readline().split()))              # arr에 땅의 한행을 input
for _ in range(row-1):                                          # 남은 행을 반복해서
    arr += list(map(int, sys.stdin.readline().split()))         # 한 행 뒤에 붙여준다

time = 500 * 500 * 2 * 257                                      # 땅고르기 시간을 저장할 변수로 모든칸의 모든 블록을 쌓을 때 걸리는 최대 시간을 저장
height = 0                                                      # 땅고르기 후 높이를 저장할 변수 생성

for e in range(257):                                            # 0부터 256층까지 반복할 때
    addblock = 0                                                # 땅을 파낸 블록을 담을 변수
    useblock = 0                                                # 땅을 쌓기위해 사용한 블록을 셀 변수
    for a in arr:                                               # 땅고르기할 지역을 반복해서
        if a - e > 0:                                           # 현재 지역이 땅고르기 후 높이보다 높으면
            addblock += (a-e)                                   # addblock에 파낸 블록을 더한다
        elif a - e < 0:                                         # 현재 지역이 땅고르기 후 높이보다 낮으면
            useblock += (e-a)                                   # useblock에 사용한 블록을 더한다
    else:                                                       # 반복이 끝나면
        if useblock-addblock <= inventory:                      # 사용한 block이 inventory에 저장된 block보다 같거나 작다면
            if time >= useblock + (addblock * 2):               # 현재 저장된 최소시간과 비교해서 이번층에 소요되는 시간이 더 작거나 같으면
                time = useblock + (addblock * 2)                # time을 이번층에 사용된 시간으로 저장하고
                height = e                                      # 높이를 이번층으로 저장한다
else:                                                           # 257층까지 탐색을 마쳤다면
    print(time, height)                                         # 시간과 높이를 출력한다