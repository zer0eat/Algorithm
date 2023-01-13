# 스티커_BOJ9465

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline().strip())                                               # 테스트 케이스

for t in range(T):                                                                  # 테스트 케이스를 반복해서
    N = int(sys.stdin.readline().strip())                                           # 스티커의 길이를 input 받고
    picture = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]      # 점수가 적힌 스티커를 input 받는다

    for n in range(N):                                                              # 스티커의 길이를 반복해서
        for m in range(2):                                                          # 위 아래 스티커를 반복한다
            if n == 0:                                                              # 맨 앞의 스티커라면
                pass                                                                # 패스하고
            elif n == 1:                                                            # 두번째 스티커라면
                if m == 0:                                                          # 위쪽 스티커는
                    picture[0][n] = picture[0][n] + picture[1][n-1]                 # 앞쪽의 대각 스티커의 점수의 합이 최대가 되므로 그 값으로 저장하고
                else:                                                               # 아래쪽 스티커도
                    picture[1][n] = picture[1][n] + picture[0][n-1]                 # 앞쪽의 대각 스티커의 점수의 합이 최대가 되므로 그 값으로 저장
            else:                                                                   # 세번째 스티커부터는
                if m == 0:                                                          # 위쪽 스티커라면
                    A = picture[0][n] + picture[1][n-1]                             # A에 위쪽스티커의 점수와 대각선 아래까지 점수의 합을 저장하고
                    B = picture[0][n] + max(picture[0][n-2], picture[1][n-2])       # B에 위쪽스티커의 점수와 2칸 전 스티커의 최대값을 합을 저장한 뒤
                    if A > B:                                                       # A가 더 크다면
                        picture[0][n] = A                                           # 스티커에 A의 값을 저장하고
                    else:                                                           # B가 같거나 더 크다면
                        picture[0][n] = B                                           # 스티커에 B의 값을 저장한다
                else:                                                               # 아래쪽 스티커라면
                    A = picture[1][n] + picture[0][n-1]                             # A에 아래쪽스티커의 점수와 대각선 위까지 점수의 합을 저장하고
                    B = picture[1][n] + max(picture[0][n-2], picture[1][n-2])       # B에 아래쪽스티커의 점수와 2칸 전 스티커의 최대값을 합을 저장한 뒤
                    if A > B:                                                       # A가 더 크다면
                        picture[1][n] = A                                           # 스티커에 A의 값을 저장하고
                    else:                                                           # B가 같거나 더 크다면
                        picture[1][n] = B                                           # 스티커에 B의 값을 저장한다

    print(max(picture[0][-1], picture[1][-1]))                                      # 마지막 스티커 중