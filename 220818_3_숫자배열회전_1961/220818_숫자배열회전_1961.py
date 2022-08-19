# 숫자배열회전_1961

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 함수 만들기
def turn90(arr):                                # 시계 방향으로 90도 돌리는 함수
    arr90 = [[] for _ in range(N)]              # 행렬을 돌렸을 때 담을 빈 리스트 만들기
    for i in range(N):                          # 행의 길이가 N 이면서
        for j in range(N):                      # 열의 길이가 N 일 때 반복
            arr90[i].append(arr[N-1-j][i])      # 90도 돌린 요소를 arr90 리스트에 append
    return arr90                                # 반복이 끝나면 리턴

# input 받기
T = int(input())                                # 테스트 케이스
for t in range(T):
    N = int(input())                            # 행렬의 길이
    arr = []                                    # 행렬을 받을 빈 리스트
    for n in range(N):                          # 행의 길이만큼 반복할 때
        arr.append(list(map(int, input().split())))     # arr리스트에 append 하기

    arr90 = turn90(arr)                         # arr 행렬을 90도 돌린 행렬을 arr90으로 저장
    arr180 = turn90(arr90)                      # arr90 행렬을 90도 돌린 행렬을 arr180으로 저장
    arr270 = turn90(arr180)                     # arr180 행렬을 90도 돌린 행렬을 arr270으로 저장

    print(f'#{t+1}')
    for i in range(N):
        print(*arr90[i],' ', *arr180[i], ' ', *arr270[i], sep='')



