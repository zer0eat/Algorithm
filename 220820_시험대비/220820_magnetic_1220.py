import sys
sys.stdin = open('magnetic_input.txt')

# 1번 풀이
# T = 10                                                    # 테스트 케이스
# for t in range(T):                                        # 테스트 케이스 만큼 반복 할 때
#     N = int(input())                                      # 행렬의 길이를 받는다
#     arr = []                                              # 행렬을 입력할 빈 리스트
#     for n in range(N):                                    # 행렬의 길이만큼 반복할 때
#         arr.append(list(map(int, input().split())))       # 한 행씩 input 받아 arr에 append
#
#
#     new_arr = []                                          # 각 열에서 자성을 지닌 물체만 담을 빈 리스트
#     for i in range(N):                                    # 열의 길이만큼 반복
#         col = []                                          # 하나의 열에서 자성을 지닌 물체만 담을 빈 리스트
#         for j in range(N):                                # 행의 길이만큼 반복
#             if arr[j][i] != 0:                            # 자성을 지닌 1,2만
#                 col.append(arr[j][i])                     # col에 append
#         else:                                             # 한 열의 반복이 끝나면
#             new_arr.append(col)                           # all_lst에 lst를 append
#
#
#     cnt = 0                                               # 충돌 수를 저장한 빈 변수를 지정하고
#     for e in range(len(new_arr)):                         # 열의 수 만큼 반복할 때
#         for r in range(len(new_arr[e])-1):                # 하나의 열에서 첫번째 요소부터 마지막에서 하나 전까지 반복할 때
#             if new_arr[e][r] == 1:                        # 2가 나오면 위쪽으로 모두 통과하기에 1이 나오면
#                 if new_arr[e][r + 1] == 1:                # 그 다음 요소를 확인해 1이면 통과
#                     pass
#                 elif new_arr[e][r + 1] == 2:              # 2이면 충돌이 일어나므로
#                     cnt += 1                              # 충돌수를 카운트 한다
#
#     print(f'#{t+1}', cnt)

# 2번 풀이
T = 10                                                    # 테스트 케이스
for t in range(T):                                        # 테스트 케이스 만큼 반복 할 때
    N = int(input())                                      # 행렬의 길이를 받는다
    arr = []                                              # 행렬을 입력할 빈 리스트
    for n in range(N):                                    # 행렬의 길이만큼 반복할 때
        arr.append(list(map(int, input().split())))       # 한 행씩 input 받아 arr에 append

    cnt = 0                                               # 충돌 수를 저장한 빈 변수를 지정하고
    for i in range(N):                                    # 열의 수 만큼 반복할 때
        j = 0                                             # 첫 번째 요소를 검사할 인덱스를 지정해주고
        while j < 100:                                    # 행의 끝까지 반복할 때
            if arr[j][i] != 1:                            # 요소가 1이 아니면
                j += 1                                    # 인덱스를 1 추가하고
            elif arr[j][i] == 1:                          # 요소가 1이라면
                for k in range(1, N-j):                   # 그 뒤의 요소를 확인하기 위해 남은 요소만큼 반복한다
                    if arr[j + k][i] == 2:                # 만약 2가 나왔다면
                        cnt += 1                          # 충돌 수를 1 카운트 하고
                        j = j + k + 1                     # 인덱스를 그 다음요소로 바꾼다
                        break                             # 그리고 반복문을 탈출한다
                else:                                     # 다 돌아도 2가 나오지 않는다면
                    break                                 # 반복문을 탈출한다

    print(f'#{t+1}', cnt)





