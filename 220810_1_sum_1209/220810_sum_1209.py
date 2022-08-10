# sum_1209

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 값 받기
T = 10 # 테스트 케이스
for t in range(T):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)] # 100*100의 행렬 리스트로 저장

    allsum = [] # 가로 세로 대각선 값을 더해준 값을 저장할 빈 리스트 작성
    # 가로 합을 allsum에 저장
    for i in range(100):
        width = 0
        for j in range(100):
            width += arr[i][j]
        allsum.append(width)

    # 세로 합을 allsum에 저장
    for j in range(100):
        height = 0
        for i in range(100):
            height += arr[i][j]
        allsum.append(height)

    # 대각선 합을 allsum에 저장
    diagonal_l= 0 # 왼쪽 위에서 오른쪽 아래로 가는 대각선
    diagonal_r=0 # 오른쪽 위에서 왼쪽 아래로 가는 대각선
    for i in range(100):
        diagonal_l += arr[i][i]
        diagonal_r += arr[i][99-i]
    allsum.append(diagonal_l)
    allsum.append(diagonal_r)

    # allsum에서 가장 큰 값 구하기
    biggest = 0
    for a in allsum:
        if biggest < a:
            biggest = a

    print(f'#{t+1} {biggest}')