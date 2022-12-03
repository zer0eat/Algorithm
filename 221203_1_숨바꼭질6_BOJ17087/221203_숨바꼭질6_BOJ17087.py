# 숨바꼭질6_BOJ17087

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, S = map(int, sys.stdin.readline().split())       # N 동생의 수 / S 수빈이의 위치
lst = list(map(int, sys.stdin.readline().split()))  # 동생이 있는 위치를 리스트로 input 받음

ans = []                                            # 수빈이와 동생의 거리를 저장할 리스트를 생성하고
for l in lst:                                       # 동생의 위치를 반복해서
    ans.append(abs(l - S))                          # 수빈이의 위치와의 차를 ans에 append 한다

D = 1                                               # 동생을 최소시간으로 찾을 수 있는 거리를 저장할 변수를 생성
num = min(ans)                                      # num에 ans의 요소 중 가장 작은 값을 저장한다

while num > 1:                                      # num이 1이 될때까지 반복해서
    for n in range(N):                              # 동생의 수 만큼 반복할 때
        if ans[n] % num == 0:                       # 수빈이와 동생과의 거리가 num로 나누어 떨어진다면
            pass                                    # 넘어가고
        else:                                       # 그렇지 않는다면
            num -= 1                                # num에서 -1을 하고
            break                                   # for문을 종료한다
    else:                                           # for문을 모두 돌았다면
        D = num                                     # D에 num을 저장하고
        break                                       # while문을 break 한다

print(D)                                            # 모든 동생을 찾기위한 최대 거리 D를 출력한다