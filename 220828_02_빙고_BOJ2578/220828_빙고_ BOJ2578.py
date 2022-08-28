# 빙고_ BOJ2578

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
bingo = [list(map(int, input().split())) for _ in range(5)]     # 빙고 행렬을 input 받음
call = [list(map(int, input().split())) for _ in range(5)]      # 지울 숫자를 행렬로 input 받음

# 빙고 call
mark = 0                                                        # bingo 행렬에 call한 숫자를 지우고 mark를 입력하기 위해 만든 변수
stopcall = False                                                # 3빙고가 나오면 반복을 멈추기 위한 장치

for i in range(5):                                              # call을 순서대로 부르기 위해 행을 순서대로
    for j in range(5):                                          # 열을 순서대로 반복할때
        mark -= 1                                               # bingo판에 나온 숫자를 표시하기 위한 mark를 -1 해주고
        C = call[i][j]                                          # call한 숫자를 C에 저장한다

        # 빙고 지우기
        flag = False                                            # 숫자를 지우면 반복문을 종료할 flag를 만들고
        for u in range(5):                                      # bingo 판을 탐색하며 call한 숫자를 지우기 위해 행을 차례대로 반복하고
            for o in range(5):                                  # 열을 차례대로 반복할 때
                if bingo[u][o] == C:                            # call한 숫자 C가 나오면
                    bingo[u][o] = mark                          # 숫자를 mark로 바꿔준다
                    flag = True                                 # 숫자를 찾았으면 flag를 바꾸고
                    break                                       # 반복문을 종료한다
            if flag == True:                                    # flag가 True일때
                break                                           # 이중 반복문도 종료한다

        # 빙고 확인하기

        if mark <= -12:                                         # 빙고의 최소조건인 12 call이 넘으면
            bingo3 = 0                                          # 3빙고를 확인하기 위한 변수를 만들고
            # 가로빙고 확인
            for k in range(5):                                  # 가로에서는 행을 반복하고 / 세로에서는 열을 반복한다
                for h in range(5):                              # 열을 반복하여
                    if bingo[k][h] < 0:                         # 해당 요소가 mark한 음수이면 패스하고
                        pass
                    else:                                       # mark가 안 된 양수가 나오면 break 한다
                        break
                else:                                           # 만약 모든 열을 반복하면
                    bingo3 += 1                                 # 한 행의 모든 요소가 음수이므로 빙고를 1 추가한다

                # 세로빙고 확인
                for d in range(5):                              # 열을 반복하여
                    if bingo[d][k] < 0:                         # 해당 요소가 mark한 음수이면 패스하고
                        pass
                    else:                                       # mark가 안 된 양수가 나오면 break 한다
                        break
                else:                                           # 만약 모든 열을 반복하면
                    bingo3 += 1                                 # 한 행의 모든 요소가 음수이므로 빙고를 1 추가한다

            # 대각선빙고(좌상>우하) 확인
            for s in range(5):                                  # 대각선을 확인하기 위해 5개를 반복하면
                if bingo[s][s] < 0:                             # 좌상>우하의 요소가 mark한 음수면 패스
                    pass
                else:                                           # mark가 안 된 양수가 나오면 break 한다
                    break
            else:                                               # 만약 반복문을 모두 돌면
                bingo3 += 1                                     # 대각선의 모든 요소가 음수이므로 빙고를 1 추가한다

            # 대각선빙고(우상>좌하) 확인
            for a in range(5):                                  # 대각선을 확인하기 위해 5개를 반복하면
                if bingo[4 - a][a] < 0:                         # 우상>좌하의 요소가 mark한 음수면 패스
                    pass
                else:                                           # mark가 안 된 양수가 나오면 break 한다
                    break
            else:                                               # 만약 반복문을 모두 돌면
                bingo3 += 1                                     # 대각선의 모든 요소가 음수이므로 빙고를 1 추가한다

            # 빙고 개수 확인
            if bingo3 >= 3:                                     # 만약 빙고가 3개 이상이면
                print(abs(mark))                                # call한 숫자인 mark를 양수로 출력하고
                stopcall = True                                 # 반복문을 깰 stopcall을 Ture로 설정하고
                break                                           # 반복문을 종료한다

    if stopcall == True:                                        # stopcall을 Ture일때
        break                                                   # 반복문을 종료한다
