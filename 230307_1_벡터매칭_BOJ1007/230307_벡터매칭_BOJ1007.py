# 벡터매칭_BOJ1007

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

def vector(n):
    global N, ans                                               # 점의 개수와 정답을 저장할 변수를 global로 불러오고
    if n == N:                                                  # n이 점의개수와 동일하다면
        if sum(bit) == N//2:                                    # bit 중 1인 것이 점의 수의 절반일 때만
            tmpx = 0                                            # x의 좌표를 저장할 변수를 생성하고
            tmpy = 0                                            # y의 좌표를 저장할 변수를 생성한다
            for b in range(N):                                  # 점의 개수만큼 반복해서
                if bit[b] == 1:                                 # 해당 위치의 bit가 1이라면
                    tmpx += lst[b][0]                           # x좌표의 변수에 점의 x값을 더해주고
                    tmpy += lst[b][1]                           # y좌표의 변수에 점의 y값을 더해주고
                else:                                           # 해당 위치의 bit가 0이라면
                    tmpx -= lst[b][0]                           # x좌표의 변수에 점의 x값을 빼주고
                    tmpy -= lst[b][1]                           # y좌표의 변수에 점의 y값을 빼주고
            else:                                               # 모든 점을 반복했다면
                distance = math.sqrt((tmpx)**2 + (tmpy)**2)     # 원점과 벡터의 합이 표현하는 점까지의 거리를 구하고
                if ans > distance:                              # ans보다 새로 구한 거리가 짧다면
                    ans = distance                              # ans를 distance로 바꿔 저정한 후
        return                                                  # return 한다
    bit[n] = 1                                                  # n이 점의개수보다 적다면 n인덱스의 요소를 1로 바꾸고
    vector(n+1)                                                 # 다음 요소를 vector 함수로 탐색한다
    bit[n] = 0                                                  # n인덱스의 요소를 0으로 바꾸고
    vector(n+1)                                                 # 다음 요소를 vector 함수로 탐색한다
    
# input 받기
T = int(input())                                                # T 테스트케이스
for t in range(T):                                              # 테스트 케이스를 반복해서
    N = int(input())                                            # N 점의 개수
    lst = [list(map(int,input().split())) for _ in range(N)]    # 점의 좌표를 리스트형태로 input 받아 list에 저장
    ans = 1e9                                                   # 벡터의 최소값을 저장할 변수 생성
    bit = [0]*N                                                 # 점의 개수만큼 bit 생성
    vector(0)                                                   # 백터함수를 통해 ans를 구하고
    print(ans)                                                  # 벡터의 최소값을 출력한다