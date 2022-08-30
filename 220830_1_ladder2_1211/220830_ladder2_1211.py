# ladder2_1211

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10                                                              # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스만큼 반복
    N = int(input())                                                # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]     # 사다리를 행렬로 받음

    start = []                                                      # 0번 행에서 1인 숫자의 행렬을 받을 리스트
    for q in range(100):                                            # 열을 반복할 때
        if arr[0][q] == 1:                                          # 0행에서 1이 나오는 것을
            start.append([0,q])                                     # start에 append

    # 델타 탐색 (우 좌 하)
    dx = [0, 0, 1]
    dy = [1, -1, 0]

    end = []                                                        # 도착점을 저장할 리스트
    cnt = 0                                                         # 도착점까지 이동한 거리를 셀 변수
    while start:                                                    # 시작점이 빌때까지 반복
        a, b = start.pop(0)                                         # a, b에 행 렬을 저장
        c = b                                                       # c에 열을 저장
        visited = [[0]*100 for _ in range(100)]                     # 사다리가 지나갈 빈 행렬 생성

        cnt += 1                                                    # 시작점을 지나갔으므로 1 추가
        while a <= 99:                                              # 사다리가 도착점까지 이동했으면
            for k in range(3):                                      # 델타탐색을 해서
                if 0 <= a+dx[k] <= 99 and 0 <= b+dy[k] <= 99:       # 행렬내의 범위에서만 이동할 때
                    if arr[a+dx[k]][b+dy[k]] == 1 and visited[a+dx[k]][b+dy[k]] == 0:   # 갈수있는 길이 1이고 지도에 표시되지 않은 처음가는 길일때
                        cnt += 1                                    # 카운트를 1 세고
                        visited[a + dx[k]][b + dy[k]] = 1           # 방문지도에 1표시한 후
                        a, b = a+dx[k], b+dy[k]                     # a,b를 이동한 위치로 저장한 뒤 반복문 종료
                        break
            if a == 99:                                             # 도착지에 도착하면
                end.append([c,cnt])                                 # 출발지의 열과 이동거리를 리스트로 end에 append
                cnt = 0                                             # cnt 초기화한 후 반복문 종료
                break
    else:                                                           # 모든 출발점에서 도착지까지 도착했다면
        for i in range(len(end)-1):                                 # 거리순으로 버블정렬하여
            for j in range(len(end)-i-1):                           
                if end[j][1] < end[j + 1][1]:                        
                    end[j], end[j + 1] = end[j + 1], end[j]         # 거리가 가장 짧은 것을 뒤로 보내는 내림차순으로 정렬

        print(f'#{t+1}', end[-1][0])                                # 가장 짧은 거리를 지나간 출발점을 출력