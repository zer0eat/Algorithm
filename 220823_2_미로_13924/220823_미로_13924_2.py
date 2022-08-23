# 미로_13924

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                            # 테스트 케이스
for t in range(T):                                          # 테스트 케이스 수만큼 반복
    N = int(input())                                        # 행렬의 길이를 N으로 input
    miro = [list(map(int, input())) for n in range(N)]      # 길이가 N인 행렬을 miro에 input

    stack = [['end', 'end']]                                # 미로를 찾으며 왔던 길을 저장해 놓기 위해 stack이라는 리스트를 만들고, 종료 표시로 'end'를 미리 넣어 둔다

    # 시작점 찾기
    for i in range(N):                                      # 미로의 행의 길이 만큼 반복
        for j in range(N):                                  # 미로의 열의 길이 만큼 반복
            if miro[i][j] == 2:                             # 시작점을 찾았다면
                a = i                                       # 행을 a에 저장
                b = j                                       # 열을 b에 저장


    # 미로 찾기 (위 오른쪽 왼쪽 아래)
    while a != 'end':                                       # stack에 미리 넣어놨던 end가 나올 때까지 반복
        if a != 0 and miro[a - 1][b] == 0:                  # 맨 위 행렬이 아니면서, 윗칸의 요소가 0이면
            stack.append([a, b])                            # 좌표를 리스트 형태로 스택에 append
            a -= 1                                          # 행의 위치를 -1하고
            miro[a][b] = 4                                  # miro 행렬에 지나간 길이라는 표시로 4를 입력한 후


        elif b != N-1 and miro[a][b + 1] == 0:              # 맨 오른쪽 행렬이 아니면서, 오른쪽칸의 요소가 0이면
            stack.append([a, b])                            # 좌표를 리스트 형태로 스택에 append
            b += 1                                          # 열의 위치를 +1하고
            miro[a][b] = 4                                  # miro 행렬에 지나간 길이라는 표시로 4를 입력한 후


        elif b != 0 and miro[a][b - 1] == 0:                # 맨 왼쪽 행렬이 아니면서, 왼쪽칸의 요소가 0이면
            stack.append([a, b])                            # 좌표를 리스트 형태로 스택에 append
            b -= 1                                          # 열의 위치를 -1하고
            miro[a][b] = 4                                  # miro 행렬에 지나간 길이라는 표시로 4를 입력한 후


        elif a != N-1 and miro[a + 1][b] == 0:              # 맨 아래 행렬이 아니면서, 아래칸의 요소가 0이면
            stack.append([a, b])                            # 좌표를 리스트 형태로 스택에 append
            a += 1                                          # 행의 위치를 +1하고
            miro[a][b] = 4                                  # miro 행렬에 지나간 길이라는 표시로 4를 입력한 후


        elif a != 0 and miro[a - 1][b] == 3:                # 맨 위 행렬이 아니면서, 윗칸의 요소가 도착점이면
            print(f'#{t + 1} 1')                            # 1을 출력하고 반복문을 break
            break
        elif b != N - 1 and miro[a][b + 1] == 3:            # 맨 오른쪽 행렬이 아니면서, 오른쪽칸의 요소가 도착점이면
            print(f'#{t + 1} 1')                            # 1을 출력하고 반복문을 break
            break
        elif b != 0 and miro[a][b - 1] == 3:                # 맨 왼쪽 행렬이 아니면서, 왼쪽칸의 요소가 도착점이면
            print(f'#{t + 1} 1')                            # 1을 출력하고 반복문을 break
            break
        elif a != N - 1 and miro[a + 1][b] == 3:            # 맨 아래 행렬이 아니면서, 아래칸의 요소가 도착점이면
            print(f'#{t + 1} 1')                            # 1을 출력하고 반복문을 break
            break

        else:                                               # 만약 막다른 길에 도달한다면
            res = stack.pop()                               # 스택에서 pop을 해서 한칸 전으로 돌아간다
            a = res[0]                                      # 전칸으로 돌아가기 위해 pop한 리스트의 0번째 인덱스를 행의 값인 a의 값으로 변경
            b = res[1]                                      # 전칸으로 돌아가기 위해 pop한 리스트의 1번째 인덱스를 열의 값인 b의 값으로 변경
    else:                                                   # 만약 해당사항이 없다면 시작점과 도착점이 연결되지 않았으므로
        print(f'#{t + 1} 0')                                # 0을 출력한다
