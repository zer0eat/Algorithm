# 농작물수확하기_2805

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):
    N = int(input())                            # N = 밭(행렬)의 길이
    farm = []                                   # 행렬을 받을 빈 리스트 생성
    for n in range(N):                          # 행의 수만큼 반복할 때
        farm.append(list(map(int, input())))    # 각 행의 farm 리스트에 append

    # 수확하기
    crop = 0                                    # 수확한 곳의 요소의 합을 받을 변수
    A = N//2                                    # 마름모 모양으로 수확할 때 반이 되는 인덱스

    # 수확 구역의 반으로 나눠 가운데를 포함한 위쪽 수확하기
    for i in range(A+1):                        # 마름모 반쪽의 위의 행을 반복할 때
        for j in range((A-i), (A-i) + 2*i + 1): # 첫번째 칸의 가운데에서 시작해서 행을 넘어갈 때 양 쪽으로 2개씩 늘어나는 범위로 반복
            crop += farm[i][j]                  # 해당 지역의 농작물을 수확하여 crop에 더하기

    # 수확 구역의 반으로 나눠 가운데를 포함하지 않은 아래쪽 수확하기
    for i in range(A+1, N):                     # 마름모 반쪽의 가운데를 제외한 아래의 행을 반복할 때
        for j in range((i-A), (i-A) + 2*(N-1-i)+1): # 가운데 칸의 다음행에서 시작해서 행을 넘어갈 때 양 쪽으로 2개씩 줄어드는 범위로 반복
            crop += farm[i][j]                  # 해당 지역의 농작물을 수확하여 crop에 더하기

    print(f'#{t + 1}', crop)
