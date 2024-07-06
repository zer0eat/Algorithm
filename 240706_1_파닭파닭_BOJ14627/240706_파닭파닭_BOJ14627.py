# 파닭파닭_BOJ14627

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S, C = map(int, input().split())        # 파와 치킨의 수를 input 받고
L = [int(input()) for _ in range(S)]    # 파의 길이를 리스트로 input 받는다
pa = 0                                  # 최대로 넣을 파를 저장할 변수를 생성하고
l, r = 1, max(L)                        # 파의 최소 최대 길이를 변수로 생성한다
while l <= r:                           # 파의 최소길이가 최대길이보다 커질때까지 반복해서
    m = (l + r)//2                      # 두 길이의 중점을 구하고
    tmp = 0                             # 파의 개수를 저장할 변수를 생성한다
    for n in L:                         # 파의 수를 반복해서
        tmp += n//m                     # m개의 길이로 자를 수 있는 파의 수를 더해준다
    if tmp < C:                         # 파의 수가 C보다 작다면
        r = m-1                         # 최대 파의 길이를 감소시킨다
    else:                               # 파의 수가 C와 같거나 크다면
        pa = max(pa, m)                 # 최대 파의 길이를 저장하고
        l = m+1                         # 최소 파의 길이를 증가시킨다
print(sum(L) - C*pa)                    # 남의 파의 길이를 출력한다