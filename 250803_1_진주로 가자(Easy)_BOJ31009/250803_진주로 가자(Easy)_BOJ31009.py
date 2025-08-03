# 진주로 가자(Easy)_BOJ31009

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 교통편의 수를 input받고
L = []                          # 교통편의 가격을 저장할 리스트를 생성하고
jinju = 0                       # 진주 가는 교통편의 가격을 저장할 변수를 생성한다
for n in range(N):              # 교통편의 수를 반복해서
    D, C = input().split()      # 교통편과 가격을 input받고
    if D == 'jinju':            # 교통편이 진주라면
        jinju = int(C)          # 가격을 저장하고
    else:                       # 교통편이 진주가 아니라면
        L.append(int(C))        # 가격을 리스트에 append한다
ans = 0                         # 정답을 저장할 변수를 생성하고
for l in L:                     # 교통편의 가격을 반복해서
    if jinju < l:               # 진주보다 비싸다면
        ans += 1                # 개수를 추가한다
print(jinju)                    # 진주가는 가격을 출력하고
print(ans)                      # 진주보다 비싼 교통편의 수를 출력한다