# 정수 좌표의 개수_BOJ16970

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def gcd(a, b):
    while b > 0:                                                # b가 0이 될때까지 반복해서
        a, b = b, a % b                                         # a에 b를 저장하고 b에 a를 b로 나눈 나머지를 저장한다
    return a                                                    # b가 0일 때 최대공약수인 a를 return한다

N, M, K = map(int, input().split())                             # N x좌표가 올 수 있는 최대값 / M y좌표가 올 수 있는 최대값 / K 점의 개수를 input 받고
cnt = 0                                                         # 선분의 개수를 셀 변수를 생성한다
for x1 in range(N+1):                                           # 시작 점의 x좌표를 반복하고
    for y1 in range(M+1):                                       # 시작 점의 y좌표를 반복하고
        for x2 in range(N+1):                                   # 끝 점의 x좌표를 반복하고
            for y2 in range(M+1):                               # 끝 점의 y좌표를 반복해서
                if gcd(abs(x2 - x1), abs(y2 - y1)) + 1 == K:    # x의 증가량과 y의 증가량의 최대 공약수를 구해 지나가는 좌표의 수를 구해서 K와 같다면
                    cnt += 1                                    # 선분의 개수를 1 추가한다
print(cnt//2)                                                   # 시작과 끝점이 반대로 결정되어 중복되므로 전체 개수의 절반만 출력한다