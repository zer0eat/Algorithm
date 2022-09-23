# 격자판의숫자이어붙이기_2819

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                        # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복할 때
    arr = [list(input().split()) for _ in range(4)]     # 행렬을 리스트로 받고

    ans = set()                                         # 정답을 저장할 빈 리스트를 만든다

    dx = [-1, 0, 1, 0]                                  # 상우하좌를 탐색할 행의 인덱스
    dy = [0, 1, 0, -1]                                  # 상우하좌를 탐색할 열의 인덱스

    tmp = []                                            # 7개를 고른 값을 저장할 리스트
    for i in range(4):                                  # 행을 반복하고
        for j in range(4):                              # 열을 반복해서 시작점을 찾는다
            tmp.append(arr[i][j])                       # 시작점이 첫번째 번호이므로 tmp에 append
            for a in range(4):                              # 상우하좌 네방향을 탐색을할 때
                if 0 <= i+dx[a] < 4 and 0 <= j+dy[a] < 4:   # 행렬의 인덱스 범위 내에서
                    tmp.append(arr[i+dx[a]][j+dy[a]])       # 두번째 번호를 tmp에 append
                    ai = i+dx[a]                            # 기준점을 현재 두번째 번호의 요소로 바꾸기 위해 행을 ai로 새로 저장
                    aj = j+dy[a]                            # 기준점을 현재 두번째 번호의 요소로 바꾸기 위해 열을 aj로 새로 저장
                    for b in range(4):                                      # 상우하좌 네방향을 탐색을할 때
                        if 0 <= ai + dx[b] < 4 and 0 <= aj + dy[b] < 4:     # 행렬의 인덱스 범위 내에서
                            tmp.append(arr[ai + dx[b]][aj + dy[b]])         # 세번째 번호를 tmp에 append
                            bi = ai + dx[b]                                 # 기준점을 현재 세번째 번호의 요소로 바꾸기 위해 행을 bi로 새로 저장
                            bj = aj + dy[b]                                 # 기준점을 현재 세번째 번호의 요소로 바꾸기 위해 열을 bj로 새로 저장
                            for c in range(4):                                      # 상우하좌 네방향을 탐색을할 때
                                if 0 <= bi + dx[c] < 4 and 0 <= bj + dy[c] < 4:     # 행렬의 인덱스 범위 내에서
                                    tmp.append(arr[bi + dx[c]][bj + dy[c]])         # 네번째 번호를 tmp에 append
                                    ci = bi + dx[c]                                 # 기준점을 현재 네번째 번호의 요소로 바꾸기 위해 행을 ci로 새로 저장
                                    cj = bj + dy[c]                                 # 기준점을 현재 네번째 번호의 요소로 바꾸기 위해 열을 cj로 새로 저장
                                    for d in range(4):                                      # 상우하좌 네방향을 탐색을할 때
                                        if 0 <= ci + dx[d] < 4 and 0 <= cj + dy[d] < 4:     # 행렬의 인덱스 범위 내에서
                                            tmp.append(arr[ci + dx[d]][cj + dy[d]])         # 다섯번째 번호를 tmp에 append
                                            di = ci + dx[d]                                 # 기준점을 현재 다섯번째 번호의 요소로 바꾸기 위해 행을 di로 새로 저장
                                            dj = cj + dy[d]                                 # 기준점을 현재 디섯번째 번호의 요소로 바꾸기 위해 열을 dj로 새로 저장
                                            for e in range(4):                                      # 상우하좌 네방향을 탐색을할 때
                                                if 0 <= di + dx[e] < 4 and 0 <= dj + dy[e] < 4:     # 행렬의 인덱스 범위 내에서
                                                    tmp.append(arr[di + dx[e]][dj + dy[e]])         # 여섯번째 번호를 tmp에 append
                                                    ei = di + dx[e]                                 # 기준점을 현재 여섯번째 번호의 요소로 바꾸기 위해 행을 ei로 새로 저장
                                                    ej = dj + dy[e]                                 # 기준점을 현재 여섯번째 번호의 요소로 바꾸기 위해 열을 ej로 새로 저장
                                                    for f in range(4):                                      # 상우하좌 네방향을 탐색을할 때
                                                        if 0 <= ei + dx[f] < 4 and 0 <= ej + dy[f] < 4:     # 행렬의 인덱스 범위 내에서
                                                            tmp.append(arr[ei + dx[f]][ej + dy[f]])         # 일곱번째 번호를 tmp에 append
                                                            ans.add(tuple(tmp))                             # 완성된 tmp를 ans에 add
                                                            tmp.pop()                                       # 마지막 글자를 빼고 for를 반복
                                                    else:                                                   # 반복이 끝났다면
                                                        tmp.pop()                                           # 마지막 글자를 뺀다
                                            else:                                                   # 반복이 끝났다면
                                                tmp.pop()                                           # 마지막 글자를 뺀다
                                    else:                                                   # 반복이 끝났다면
                                        tmp.pop()                                           # 마지막 글자를 뺀다
                            else:                                                   # 반복이 끝났다면
                                tmp.pop()                                           # 마지막 글자를 뺀다
                    else:                                                   # 반복이 끝났다면
                        tmp.pop()                                           # 마지막 글자를 뺀다
            else:                                                   # 반복이 끝났다면
                tmp.pop()                                           # 마지막 글자를 뺀다

    print(f'#{t+1}', len(ans))


