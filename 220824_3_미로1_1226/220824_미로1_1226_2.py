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
    stack = [[1, 1]]                                            # 미로를 찾으며 왔던 길을 저장해 놓기 위해 stack이라는 리스트를 만들고, 시작점을 미리 넣어 둔다

    while stack:                                                # stack이 빌 때까지 반복
        a, b = stack.pop()                                      # 검사할 지점을 스택에서 pop하여 꺼낸다
        if miro[a + 1][b] == 3 or miro[a][b + 1] == 3 or miro[a][b - 1] == 3 or miro[a - 1][b] == 3:
            print(f'#{case} 1')                                 # 현재 위치를 중심으로 1칸 이동했을 때 도착점이 존재하면 1을 출력하고
            break                                               # 반복문 종료
        if miro[a + 1][b] == 0:                                 # 아래칸의 요소가 0이면
            a += 1                                              # 행의 위치를 +1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            a -= 1                                              # 원래 자리로 돌아온다
        if miro[a][b + 1] == 0:                                 # 오른쪽칸의 요소가 0이면
            b += 1                                              # 열의 위치를 +1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            b -= 1                                              # 원래 자리로 돌아온다
        if miro[a][b - 1] == 0:                                 # 왼쪽칸의 요소가 0이면
            b -= 1                                              # 열의 위치를 -1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            b += 1                                              # 원래 자리로 돌아온다
        if miro[a - 1][b] == 0:                                 # 윗칸의 요소가 0이면
            a -= 1                                              # 행의 위치를 -1하고
            miro[a][b] = 4                                      # 방문표시로 4를 입력한다
            stack.append([a, b])                                # 좌표를 리스트 형태로 스택에 append
            a += 1                                              # 원래 자리로 돌아온다
    else:                                                       # 만약 해당사항이 없다면 시작점과 도착점이 연결되지 않았으므로
        print(f'#{case} 0')                                     # 0을 출력한다
