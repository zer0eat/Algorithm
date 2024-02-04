# 보석상자_BOJ2792

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # N 아이들의 수 / M 보석의 종류를 input 받고
color = [int(input()) for _ in range(M)]    # 색상별 보석의 수를 리스트로 input 받는다
l = 1                                       # 보석의 최소수를 저장하고
r = max(color)                              # 보석의 최대수를 저장한 후
while l <= r:                               # 보석의 최소수가 최대수보다 커질때 까지 반복해서
    tmp = 0                                 # 나눠줄 사람의 수를 저장할 변수를 생성하고
    m = (l+r)//2                            # 최대와 최수의 중간값을 나눠줄 개수로 저장한다
    for c in color:                         # 보석을 반복해서
        if c%m:                             # m개로 나눴을 때 나머지가 있다면
            tmp += c//m + 1                 # tmp에 나눠줄 사람의 수를 c//m+1을 더해주고
        else:                               # m개로 나눴을 때 나머지가 없다면
            tmp += c//m                     # tmp에 나눠줄 사람의 수를 c//m을 더해준다
    if tmp <= N:                            # tmp가 N보다 작거나 같다면
        r = m-1                             # 최대 보석수를 m-1로 저장하고
    else:                                   # tmp가 N보다 크다면
        l = m+1                             # 최소 보석수를 m+1로 저장한다
print(l)                                    # 한사람에게 나눠줄 최대 보석의 수를 출력한다