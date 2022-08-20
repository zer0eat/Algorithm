import sys
sys.stdin = open('스도쿠검증_input.txt')

T = int(input())                                            # 테스트 케이스
for t in range(T):
    sudoku = []                                             # 스도쿠를 받을 빈 리스트
    for n in range(9):                                      # 스도쿠의 길이만큼 반복할 때
        sudoku.append(list(map(int, input().split())))      # 빈리스트에 스도쿠의 행을 추가한다

    stop = False                                            # 멈춤 신호를 주기 위한 장치

    for i in range(9):                                      # 스도쿠의 길이만큼 반복
        lst = []                                            # 스도쿠의 열을 담을 빈 리스트
        for j in range(9):                                  # 스도쿠의 길이만큼 반복
            lst.append(sudoku[j][i])                        # 빈 리스트에 열의 각 요소를 append
        else:                                               # 반복이 완료되면
            rowset = set(sudoku[i])                         # rowset에 행을 set로 만들어준 것을 저장
            colset = set(lst)                               # colset에 열을 set로 만들어준 것을 저장
            if len(rowset) == len(colset) == 9:             # 길이가 9이면 패스
                pass
            else:                                           # 그렇지 않으면
                print(f'#{t+1}', 0)                         # 0을 출력하고
                stop = True                                 # 반복문 멈춤 신호를 준다
                break                                       # 반복문을 깬다

    if stop == False:                                       # 반복문 멈춤 신호가 없을 때
        for i in range(0, 9, 3):                            # 스도쿠 길이를 3칸씩 뛰어넘는 반복
            if stop == False:                               # 반복문 멈춤 신호가 없을 때
                for j in range(0, 9, 3):                    # 스도쿠 길이를 3칸씩 뛰어넘는 반복
                    lst = []                                # 3X3 스도쿠를 담을 빈리스트
                    for k in range(3):                      # 작은 스도쿠의 길이만큼 반복
                        for m in range(3):                  # 작은 스도쿠의 길이만큼 반복
                            lst.append(sudoku[i+k][j+m])    # 작은 스도쿠의 요소를 모두 리스트에 append
                    else:                                   # 반복이 끝나면
                        minisudoku = set(lst)               # lst를 set으로 만들어 저장
                        if len(minisudoku) == 9:            # set의 길이가 9라면 패스
                            pass
                        else:                               # 그렇지 않다면
                            print(f'#{t + 1}', 0)           # 0을 출력하고
                            stop = True                     # 멈춤 신호를 준다
                            break                           # 반복문을 끝낸다
            else:                                           # 멈춤 신호가 있다면
                break                                       # 반복문을 끝낸다

        else:                                               # 모든 검사를 통과하면
            print(f'#{t + 1}', 1)                           # 1을 출력한다