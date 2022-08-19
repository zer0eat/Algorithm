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
    start = N//2                                # 마름모 모양으로 수확할 때 반이 되는 인덱스
    end = N//2                                  # 마름모 모양으로 수확할 때 반이 되는 인덱스

    for i in range(N):                          # 마름모의 행을 반복할 때
        for j in range(start, end + 1):         # 0번째 행에서 가운데 요소만 수확한다
            crop += farm[i][j]                  # 수확한 값을 crop에 추가한다

        if i < N // 2:                          # 만약 마름모의 반을 지나지 않았다면
            start -= 1                          # 시작점을 뒤로 한칸
            end += 1                            # 끝나는 점을 앞으로 한칸 이동한다
        else:                                   # 만약 마름모의 반을 지났다면
            start += 1                          # 시작점을 앞으로 한칸
            end -= 1                            # 끝나는 점을 뒤로 한칸 이동한다

    print(f'#{t + 1}', crop)
