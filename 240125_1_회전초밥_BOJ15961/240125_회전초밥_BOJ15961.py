# 회전초밥_BOJ15961

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, D, K, C = map(int, input().split())      # N 접시의 수 / D 초밥의 종류 / K 먹을 수 있는 초밥의 개수 / C 쿠폰 번호를 input 받고
sushi = [int(input()) for _ in range(N)]    # 초밥의 접시를 리스트로 input 받는다
eat = [0]*(D+1)                             # 먹은 초밥을 저장할 리스트를 생성하고
cnt = 0                                     # 먹은 초밥의 종류를 저장할 변수를 생성하고
flag = True                                 # 쿠폰으로 제공되는 초밥을 먹었는지 체크할 변수를 생성하고
for k in range(K):                          # 연속으로 먹을 초밥의 개수를 반복해서
    if sushi[k] == C:                       # 쿠폰에 적혀 있는 초밥을 먹었다면
        flag = False                        # flag를 False로 바꿔주고
    if eat[sushi[k]] == 0:                  # 처음 먹는 초밥이라면
        cnt += 1                            # cnt의 수를 하나 증가시키고
    eat[sushi[k]] += 1                      # sushi[k]의 초밥을 먹은 수를 1 증가시킨다
ans = cnt+flag                              # ans에 현재 먹은 초밥의 종류를 저장하고
for s in range(N):                          # 초밥의 접시의 수를 반복해서
    if eat[sushi[s]] == 1:                  # s번째 초밥이 한개 먹었던 경우에
        cnt -= 1                            # 종류를 1 감소시키고
        if sushi[s] == C:                   # s번째 초밥이 C인 경우라면
            flag = True                     # flag를 True로 바꿔준 후
    eat[sushi[s]] -= 1                      # s번째 초밥의 수를 1 감소시킨다
    t = (s+K)%N                             # s+k번째 초밥을 N으로 나눠 회전하는 인덱스로 만들어준 후
    if eat[sushi[t]] == 0:                  # t번째 초밥을 처음먹는 경우에는
        cnt += 1                            # cnt를 1 증가시키고
        if sushi[t] == C:                   # t번째 초밥이 C인 경우라면
            flag = False                    # flag를 False로 바꿔준 후
    eat[sushi[t]] += 1                      # t번째 초밥의 수를 1 증가시킨다
    ans = max(ans, cnt + flag)              # ans에 가장 많이 먹은 초밥의 종류의 수를 저장하고
print(ans)                                  # 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값을 하나의 정수로 출력한다