# 피터팬 프레임_BOJ3054

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
W = input().strip()                             # 문자를 input 받고
N = len(W)                                      # 문자의 길이를 저장한다
for i in range(5):                              # 피터팬 프레임의 5줄을 반복해서
    if i == 0 or i == 4:                        # 1,5번째 줄이라면
        for j in range(1,N+1):                  # 문자의 길이를 반복해서
            if j % 3:                           # 3번째 문자가 아니라면
                print('..#.', end='')           # #으로 피터팬 프레임을 출력하고
            else:                               # 3번째 문자라면
                print('..*.', end='')           # *로 피터팬 프레임을 출력한다
            if j == N:                          # 문자의 마지막까지 반복했다면
                print('.')                      # .을 출력하고 줄을 바꾼다
    elif i == 1 or i ==3:                       # 2,4번째 줄이라면
        for j in range(1,N+1):                  # 문자의 길이를 반복해서
            if j % 3:                           # 3번째 문자가 아니라면
                print('.#.#', end='')           # #으로 피터팬 프레임을 출력하고
            else:                               # 3번째 문자라면
                print('.*.*', end='')           # *로 피터팬 프레임을 출력한다
            if j == N:                          # 문자의 마지막까지 반복했다면
                print('.')                      # .을 출력하고 줄을 바꾼다
    elif i == 2:                                # 3번째 줄이라면
        for j in range(1,N+1):                  # 문자의 길이를 반복해서
            if j == 1 or j % 3 and j % 3 != 1:  # 3번째 문자가 아니라면
                print(f'#.{W[j-1]}.', end='')   # #으로 피터팬 프레임을 출력하고
            else:                               # 3번째 문자라면
                print(f'*.{W[j-1]}.', end='')   # *로 피터팬 프레임을 출력한다
            if j == N and j % 3:                # 문자의 마지막까지 반복하고 3의배수가 아닌 문자로 끝났다면
                print('#')                      # #을 출력하고 줄을 바꾼다
            elif j == N:                        # 문자의 마지막까지 반복하고 3의배수 문자로 끝났다면
                print('*')                      # *을 출력하고 줄을 바꾼다