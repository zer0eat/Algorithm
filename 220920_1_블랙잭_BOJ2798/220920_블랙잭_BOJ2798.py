# 블랙잭_BOJ2798

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, M = map(int, input().split())                        # N 카드의 개수 / M 블랙잭의 최대값
card = list(map(int, input().split()))                  # card를 리스트로 input

jack = 0                                                # 3장의 카드의 합을 저장할 변수
tmp = 0                                                 # jack에 저장하기 전 임시로 저장할 변수
flag = False                                            # jack의 최대값을 찾았을때 반복문을 끝낼 변수
for i in range(N):                                      # 처음 카드를 한장 뽑고
    if flag == True:                                    # jack이 최대 값이면 break
        break
    for j in range(i+1, N):                             # 처음 카드 이후에서 한장 뽑고
        if flag == True:                                # jack이 최대 값이면 break
            break
        for k in range(j+1, N):                         # 두번째 카드 이후에서 한장 뽑았을 때
            tmp = card[i] + card[j] + card[k]           # tmp에 3장의 카드의 합을 저장하고
            if tmp <= M and tmp > jack:                 # tmp가 최대값 이하이고 현재 저장된 jack보다 클때
                jack = tmp                              # jack을 tmp로 바꿔주고
                if jack == M:                           # 만약 jack이 최대값이라면
                    flag = True                         # flag를 키고 break
                    break
                tmp = 0                                 # jack이 최대값이 아니라면 tmp를 초기화
print(jack)