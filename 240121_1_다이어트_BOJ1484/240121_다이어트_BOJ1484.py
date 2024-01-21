# 다이어트_BOJ1484

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
G = int(input())                    # 몸무게의 차이를 input 받고
kgram = []                          # 몸무게의 제곱을 저장할 리스트를 생성한다
for i in range(1, 100001):          # 1부터 100000까지 반복해서
    kgram.append(i*i)               # 제곱수를 리스트에 append한다
l = 0                               # 왼쪽 수를 가르킬 포인터를 만들고
r = 1                               # 오른쪽 수를 가르킬 포인터를 만든다
ans = []                            # 정답을 저장할 리스트를 생성하고
while l < r:                        # 왼쪽이 오른쪽과 같은 곳을 가르킬때까지 반복해서
    if kgram[r] - kgram[l] == G:    # 두 몸무게의 차가 G라면
        ans.append(r+1)             # 정답에 살찌기 전 무게를 append하고
    if kgram[r] - kgram[l] > G:     # 몸무게의 차가 G보다 크다면
        l += 1                      # 살찌기 전 무게를 증가시키고
    else:                           # 몸무게의 차가 G보다 작다면
        r += 1                      # 살찐 후 무게를 증가시킨다
if ans:                             # 정답이 있다면
    for a in ans:                   # 정답을 반복해서
        print(a)                    # 하나씩 출력하고
else:                               # 정답이 없다면
    print(-1)                       # -1을 출력한다