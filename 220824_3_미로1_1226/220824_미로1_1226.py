# 미로1_1226

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                                          # 테스트 케이스
for t in range(T):                                              # 테스트 케이스만큼 반복할 때
    case = int(input())                                         # 테스트 케이스 번호
    miro = [list(map(int, input())) for _ in range(16)]         # 미로를 행렬 형태로 받은 리스트

    # 시작점 설정
    a = 1                                                       # 시작점의 행의 인덱스
    b = 1                                                       # 시작점의 열의 인덱스

    # 미로 찾기
    stack = [['end', 'end']]                                    # 미로를 찾으며 왔던 길을 저장해 놓기 위해 stack이라는 리스트를 만들고, 종료 표시로 'end'를 미리 넣어 둔다

    while a != 'end':                                           # stack에 미리 넣어놨던 end가 나올 때까지 반복
        if miro[a + 1][b] == 3 or miro[a][b + 1] == 3 or miro[a][b - 1] == 3 or miro[a - 1][b] == 3:
            print(f'#{case} 1')                                 # 현재 위치를 중심으로 1칸 이동했을 때 도착점이 존재하면 1을 출력하고
            break                                               # 반복문 종료
        elif miro[a + 1][b] == 0:                               # 아래칸의 요소가 0이면
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            a += 1                                              # 행의 위치를 +1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
        elif miro[a][b + 1] == 0:                               # 오른쪽칸의 요소가 0이면
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            b += 1                                              # 열의 위치를 +1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
        elif miro[a][b - 1] == 0:                               # 왼쪽칸의 요소가 0이면
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            b -= 1                                              # 열의 위치를 -1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
        elif miro[a - 1][b] == 0:                               # 윗칸의 요소가 0이면
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            a -= 1                                              # 행의 위치를 -1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
        else:                                                   # 만약 막다른 길에 도달한다면
            tmp = stack.pop()                                   # 스택에서 pop을 해서 한칸 전으로 돌아간다
            a = tmp[0]                                          # 전칸으로 돌아가기 위해 pop한 리스트의 0번째 인덱스를 행의 값인 a의 값으로 변경
            b = tmp[1]                                          # 전칸으로 돌아가기 위해 pop한 리스트의 1번째 인덱스를 열의 값인 b의 값으로 변경
    else:                                                       # 만약 해당사항이 없다면 시작점과 도착점이 연결되지 않았으므로
        print(f'#{case} 0')                                     # 0을 출력한다
