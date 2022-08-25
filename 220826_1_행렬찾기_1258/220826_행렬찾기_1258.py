# 행렬찾기_1258

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from pprint import pprint

# input 받기
T = int(input())                                                        # 테스트 케이스
for t in range(T):                                                      # 테스트 케이스만큼 반복해서
    N = int(input())                                                    # N = 행렬의 길이
    chemical = [list(map(int, input().split())) for _ in range(N)]      # 길이가 N인 행렬을 chemical 리스트에 받음
    find_chemical = [[0]*N for _ in range(N)]                           # 화학물질이 있는 곳을 표시할 빈 행렬을 만듬

    # 화학물질 출발점 찾기
    sp = []                                                             # sp = start point 시작점을 저장할 빈 리스트

    for i in range(N):                                                  # 행렬의 행을 반복하고
        for j in range(N):                                              # 행렬의 열을 반복할때
            if i == 0 and j == 0 and chemical[i][j] != 0:               # 만약 (0,0)의 요소가 0이 아닐 때
                find_chemical[i][j] += 1                                # find_chemical[i][j]에 1을 추가하고
                sp.append(i)                                            # sp 리스트에 행과
                sp.append(j)                                            # sp 리스트에 열을 저장한다

            elif i-1 < 0:                                               # 행의 인덱스가 0일 때
                if chemical[i][j] != 0 and chemical[i][j-1] == 0:       # 찾는 요소가 0이 아니고 그 왼쪽칸도 0일 때
                    find_chemical[i][j] += 1                            # find_chemical[i][j]에 1을 추가하고
                    sp.append(i)                                        # sp 리스트에 행과
                    sp.append(j)                                        # sp 리스트에 열을 저장한다

            elif j-1 < 0:                                               # 열의 인덱스가 0일 때
                if chemical[i][j] != 0 and chemical[i-1][j] == 0:       # 찾는 요소가 0이 아니고 그 윗칸도 0일 때
                    find_chemical[i][j] += 1                            # find_chemical[i][j]에 1을 추가하고
                    sp.append(i)                                        # sp 리스트에 행과
                    sp.append(j)                                        # sp 리스트에 열을 저장한다

            elif i-1 >= 0 and j-1 >= 0:                                 # 행과 열의 인덱스가 0이 아니면서
                if chemical[i][j] != 0 and chemical[i-1][j] == 0 and chemical[i][j-1] == 0:     # 찾는 요소가 0이 아니고 그 윗칸도 왼쪽칸도 0일 때
                    find_chemical[i][j] += 1                            # find_chemical[i][j]에 1을 추가하고
                    sp.append(i)                                        # sp 리스트에 행과
                    sp.append(j)                                        # sp 리스트에 열을 저장한다

    cnt = len(sp) // 2                                                  # 출력할 박스의 개수는 저장된 행렬의 위치 한 쌍 당 한 개이므로 2로 나눠서 cnt에 저장

    all_box = []                                                        # 모든 박스의 행의 길이와 열의 길이를 저장할 리스트
    # 화학물질 크기 찾기
    while sp:                                                           # sp라는 q가 빌 때까지 반복한다
        x = sp.pop(0)                                                   # x = sp의 맨 앞의 값 / 시작점의 행 인덱스
        y = sp.pop(0)                                                   # y = sp의 두번째 값 / 시작점의 열 인덱스

        xc = x                                                          # 박스의 행의 길이를 구하기 위한 시작점 복제품
        yc = y                                                          # 박스의 열의 길이를 구하기 위한 시작점 복제품

        box = []                                                        # 박스 한개의 행의 길이와 열의 길이를 저장할 리스트

        # 박스의 행의 길이 찾기
        while 1:                                                        # break 되기 전까지 무한히 반복할 때
            if xc+1 == N:                                               # 만약 xc가 맨 오른쪽 인덱스라면(박스가 오른쪽 끝까지 가면 끝남)
                box.append(find_chemical[xc][yc])                       # 행의 길이를 box에 append 하고 반복문을 break
                break
            elif chemical[xc+1][yc] != 0:                               # 만약 다음 오른쪽 칸의 요소가 0이 아니라면(박스가 이어지고 있음)
                find_chemical[xc+1][yc] = find_chemical[xc][yc] + 1     # 오른쪽 칸 박스에 전칸보다 하나 큰 값을 더해서 저장하고
                xc = xc+1                                               # 행의 인덱스를 1 추가한다
                yc = yc                                                 # 열은 그대로
            elif chemical[xc + 1][yc] == 0:                             # 만약 다음 오른쪽 칸의 요소가 0이라면(다음칸에 화학물질이 없다면 박스가 끝남)
                box.append(find_chemical[xc][yc])                       # 행의 길이를 box에 append 하고 반복문을 break
                break

        # 박스의 열의 길이 찾기
        while 1:                                                        # break 되기 전까지 무한히 반복할 때
            if y+1 == N:                                                # 만약 y가 맨 아래쪽 인덱스라면(박스가 아래쪽 끝까지 가면 끝남)
                box.append(find_chemical[x][y])                         # 열의 길이를 box에 append 하고 반복문을 break
                break
            elif chemical[x][y+1] != 0:                                 # 만약 다음 아래쪽 칸의 요소가 0이 아니라면(박스가 이어지고 있음)
                find_chemical[x][y+1] = find_chemical[x][y] + 1         # 아래쪽 칸 박스에 전칸보다 하나 큰 값을 더해서 저장하고
                x = x                                                   # 행은 그대로
                y = y+1                                                 # 열의 인덱스를 1 추가한다
            elif chemical[x][y + 1] == 0:                               # 만약 다음 아래쪽 칸의 요소가 0이라면(다음칸에 화학물질이 없다면 박스가 끝남)
                box.append(find_chemical[x][y])                         # 열의 길이를 box에 append 하고 반복문을 break
                break

        all_box.append(box)                                             # 저장된 박스 한개의 행과 열의 길이를 all_box에 append

    # print(cnt)
    # print(all_box)

    # 박스 넓이 추가하기
    size = []                                                           # 박스의 크기별로 정렬하기 위해 만든 빈 리스트
    for b in range(len(all_box)):                                       # 박스의 길이가 담긴 리스트의 인덱스를 반복할 때
        tmp = []                                                        # 박스의 출발점과 크기를 저장하기 위해 만든 빈 리스트
        tmp.append(all_box[b])                                          # 0번 인덱스에는 출발점의 리스트를 넣고
        tmp.append(all_box[b][0] * all_box[b][1])                       # 1번 인덱스에는 박스의 크기를 넣는다
        size.append(tmp)                                                # size 리스트에 tmp를 넣어 출발점마다 넓이 값이 적힌 리스트를 만든다

    # print(size)

    # 크기 별로 박스 정리하기
    for s in range(len(size) - 1):                                      # 버블 솔트하여
        for s1 in range(len(size) - 1):
            if size[s1][1] > size[s1 + 1][1]:                           # 앞 요소의 넓이가 뒷 요소의 넓이보다 넓다면
                size[s1], size[s1 + 1] = size[s1 + 1], size[s1]         # 바꿔준다
            elif size[s1][1] == size[s1 + 1][1]:                        # 만약 넓이가 같을 때는
                if size[s1][0][0] > size[s1+1][0][0]:                   # 박스의 행의 크기를 비교해서
                    size[s1], size[s1 + 1] = size[s1 + 1], size[s1]     # 작은 값이 앞에 나오게 정렬한다
    # print(size)

    print(f'#{t+1}', cnt, end=' ')                                      # 테스트케이스와 박스의 개수를 출력하고
    for i in range(len(size)-1):                                        # 박스의 행과 열의 길이를 출력한다
        print(*size[i][0], end=' ')
    print(*size[-1][0])
