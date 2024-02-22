# 도영이가 만든 맛있는 음식_BOJ2961

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 재료의 수를 input 받고
taste = [list(map(int, input().split())) for _ in range(N)] # 재료의 신맛과 쓴맛을 리스트로 input 받은 후
ans = 1e9                                                   # 정답을 저장할 변수를 생성한다

def recur(dep, start, food):
    global ans                                              # ans를 global 변수로 선언하고
    t1, t2 = 1, 0                                           # 신맛과 쓴맛을 저장할 변수를 생성한다
    if dep > 0:                                             # 1가지 이상 재료가 들어갔다면
        for f in food:                                      # 음식의 재료를 반복해서
            t1 *= f[0]                                      # 신맛을 계산하고
            t2 += f[1]                                      # 쓴맛을 계산한 후
        ans = min(abs(t1-t2), ans)                          # 완성된 음식의 신맛과 쓴맛의 차가 작은 값을 저장한다
    if dep == N:                                            # 모든 재료가 들어 갔다면
        return                                              # return한다
    for i in range(start, N):                               # start 재료부터 반복해서
        food.append(taste[i])                               # 음식 리스트에 i번째 재료를 담고
        recur(dep+1, i+1, food)                             # 깊이 dep+1, i+1번째 재료부터 요리의 신맛과 쓴맛의 차를 탐색한 후
        food.pop()                                          # 음식 리스트에 i번째 재료를 뺀다

recur(0, 0, [])                                             # 깊이 0, 0번째 재료부터 요리의 신맛과 쓴맛의 차를 탐색한다
print(ans)                                                  # 신맛과 쓴맛의 차이가 가장 작은 요리의 차이를 출력한다