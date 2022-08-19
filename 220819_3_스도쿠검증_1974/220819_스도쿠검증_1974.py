# 스도쿠검증_1974

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                        # 테스트 케이스
for t in range(T):                                      # 테스트 케이스 수만큼 반복할 때
    sudoku = []                                         # 스도쿠를 담을 빈 리스트 만들기
    for a in range(9):                                  # 스도쿠의 행만큰 반복할 때
        sudoku.append(list(map(int, input().split())))  # 각 행의 값을 입력받아 sudoku에 append 한다

    # 가로 / 세로줄 확인
    row = []                                            # 가로줄의 합을 담을 빈 리스트
    col = []                                            # 세로줄의 합을 담을 빈 리스트
    for i in range(9):                                  # 스도쿠의 길이를 반복하는 반복문
        row_sum = 0                                     # 스도쿠의 행의 합을 저장할 변수
        col_sum = 0                                     # 스도쿠의 열의 합을 저장할 변수
        for j in range(9):                              # 스도쿠의 길이를 반복하는 반복문
            row_sum += sudoku[i][j]                     # 스도쿠의 한 행을 모두 row_sum에 더한다
            col_sum += sudoku[j][i]                     # 스도쿠의 한 열을 모두 col_sum에 더한다
        else:                                           # 반복이 끝나면
            row.append(row_sum)                         # 한 행의 값이 모두 더해진 row_sum을 row 리스트에 append
            col.append(col_sum)                         # 한 열의 값이 모두 더해진 col_sum을 col 리스트에 append

    # 3X3 확인
    row_col33 = []                                      # 3X3의 스도쿠의 합을 저장할 빈 리스트
    for l in range(0,9,3):                              # 스도쿠의 행을 3칸씩 뛰어넘을 반복문
        for k in range(0,9,3):                          # 스도쿠의 열을 3칸씩 뛰어넘을 반복문
            w = 0                                       # 3X3의 스도쿠의 합을 저장할 변수
            for r in range(3):                          # 스도쿠의 행을 3칸을 반복할 반복문
                q = 0                                   # 3X3의 한 행의 합을 저장할 변수
                for c in range(3):                      # 스도쿠의 열을 3칸을 반복할 반복문
                    q += sudoku[r+l][c+k]               # 3X3의 스도쿠의 한 행을 모두 q에 더한다
                else:                                   # 반복이 끝나면
                    w += q                              # 더해진 q를 w에 더한다
            else:                                       # 반복이 끝나면
                row_col33.append(w)                     # 3X3의 스도쿠의 값이 모두 더해진 w를 row_col33에 append 한다

    # 스도쿠 검증
    for p in range(9):                                  # row, col row_col33에 저장된 값을 보기 위한 반복문을 설정하고
        if row[p] == col[p] == row_col33[p] == 45:      # row[p] = col[p] = row_col33[p] = 45 일 때는 패스
            pass
        else:                                           # row[p] = col[p] = row_col33[p] = 45 가 아니면 완성되지 않은 스도쿠이므로 0을 출력하고 break
            print(f'#{t+1}', '0')
            break
    else:                                               # 반복문이 끝나면 완성된 스도쿠이므로 1을 출력한다
        print(f'#{t + 1}', '1')