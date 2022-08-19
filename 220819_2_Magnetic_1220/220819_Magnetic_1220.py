# Magnetic_1220

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                                  # 테스트 케이스
for t in range(T):                                      # 테스트 케이스 만큼 반복 할 때
    N = int(input())                                    # 행렬의 길이를 받는다
    arr = []                                            # 행렬을 입력할 빈 리스트
    for n in range(N):                                  # 행렬의 길이만큼 반복할 때
        arr.append(list(map(int, input().split())))     # 한 행씩 input 받아 arr에 append

    all_lst=[]                                          # 각 열에서 자성을 지닌 물체만 담을 빈 리스트
    for i in range(100):                                # 열의 길이만큼 반복
        lst = []                                        # 하나의 열에서 자성을 지닌 물체만 담을 빈 리스트
        for j in range(100):                            # 행의 길이만큼 반복
            if arr[j][i] != 0:                          # 자성을 지닌 1,2만
                lst.append(arr[j][i])                   # lst에 append
        else:                                           # 한 열의 반복이 끝나면
            all_lst.append(lst)                         # all_lst에 lst를 append

    cnt = 0                                             # 충돌 수를 저장한 빈 변수를 지정하고
    for b in range(len(all_lst)):                       # 열의 수 만큼 반복할 때
        for a in range(len(all_lst[b])-1):              # 하나의 열에서 첫번째 요소부터 마지막에서 하나 전까지 반복할 때
            if all_lst[b][a] == 1:                      # 2가 나오면 위쪽으로 모두 통과하기에 1이 나오면
                if all_lst[b][a+1] == 1:                # 그 다음 요소를 확인해 1이면 통과
                    pass
                elif all_lst[b][a+1] == 2:              # 2이면 충돌이 일어나므로
                    cnt += 1                            # 충돌수를 카운트 한다
    print(f'#{t+1}', cnt)
