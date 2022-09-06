# 성지키기_BOJ1236

# input.txt 열기
import sys
sys.stdin = open('input3.txt')

# input 받기
N, M = map(int, input().split())                # N은 세로의 길이 M은 가로의 길이
castle = [input() for n in range(N)]            # castle에 경비원의 위치를 리스트로 받음

cnt_r = 0                                       # 가로 줄로 탐색할 때 경비원이 없는 줄을 저장할 변수
for i in range(N):                              # 행을 반복하고
    for j in range(M):                          # 열을 반복할 때
        if castle[i][j] == '.':                 # 요소에 경비원이 없으면 패스
            pass
        else:                                   # 경비원이 있다면 반복문 break
            break
    else:                                       # 한줄 전부다 경비원이 없으면 cnt_r에 필요한 경비원을 더함
        cnt_r += 1

cnt_c = 0                                       # 세로 줄로 탐색할 때 경비원이 없는 줄을 저장할 변수
for j in range(M):                              # 열을 반복하고
    for i in range(N):                          # 행을 반복할 때
        if castle[i][j] == '.':                 # 요소에 경비원이 없으면 패스
            pass
        else:                                   # 경비원이 있다면 반복문 break
            break
    else:                                       # 한줄 전부다 경비원이 없으면 cnt_c에 필요한 경비원을 더함
        cnt_c += 1

if cnt_r > cnt_c:                               # 추가로 세울 경비원이 더 많은 줄 만큼 세우면 적은줄도 커버가 되기 때문에 더 많은 줄의 경비원 숫자를 출력
    print(cnt_r)
else:
    print(cnt_c)
