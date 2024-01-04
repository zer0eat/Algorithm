# 에너지모으기_BOJ16198

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 에너지구슬의 개수를 input 받고
W = list(map(int, input().split()))         # 에너지 구슬의 무게를 리스트로 input 받는다
ans = 0                                     # 최대 에너지를 저장할 변수를 생성하고

def energy(lst, tmp):
    global ans                              # ans를 global 변수로 선언하고
    if len(lst) == 2:                       # 에너지 구슬이 2개만 남았다면
        ans = max(tmp, ans)                 # 현재 에너지와 최대 에너지 중 더 큰 값을 ans에 저장하고
        return                              # return 한다
    for i in range(1, len(lst)-1):          # 맨 앞과 뒤를 제외한 에너지구슬을 반복해서
        WW = lst[:i] + lst[i+1:]            # i번째 구슬을 제외한 리스트를 WW에 저장하고
        energy(WW, tmp+lst[i-1]*lst[i+1])   # energy 함수를 통해 에너지를 모은다

for i in range(1, N-1):                     # 맨 앞과 뒤를 제외한 에너지구슬을 반복해서
    WW = W[:i] + W[i+1:]                    # i번째 구슬을 제외한 리스트를 WW에 저장하고
    energy(WW, W[i-1]*W[i+1])               # energy 함수를 통해 에너지를 모은다
print(ans)                                  # 최대 에너지를 출력한다