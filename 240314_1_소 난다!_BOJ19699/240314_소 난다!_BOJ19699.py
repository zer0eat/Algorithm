# 소 난다!_BOJ19699

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())        # N 소의수 / M 선별할 소의 수를 input 받고
cows = list(map(int, input().split()))  # 소의 몸무게를 리스트로 input 받는다
ans = set()                             # 선별한 소의 몸무게 합을 저장할 set을 생성한다

def recur(dep, start, tmp):
    if dep == M:                        # 선별한 소가 M마리가 된다면
        ans.add(tmp)                    # 몸무게의 합을 ans에 add한다
    for i in range(start, N):           # start부터 소를 반복해서
        recur(dep+1, i+1, tmp+cows[i])  # dep+1 깊이로 i+1번 소부터 선별한다

recur(0, 0, 0)                          # 0 깊이로 0번 소부터 선별한다
ans = list(ans)                         # 선별한 소의 몸무게가 담긴 셋을 리스트로 바꾼 후
ans2 = []                               # 소수인 몸무게의 합만 담을 리스트를 생성하고
for a in ans:                           # 선별한 소의 몸무게를 반복해서
    for b in range(2, int(a**0.5)+1):   # 해당 소의 제곱근 이하를 반복해서
        if a%b == 0:                    # 나누어 떨어진다면
            break                       # break한다
    else:                               # 소수라면
        ans2.append(a)                  # ans2에 append한다
ans2.sort()                             # ans2를 오름차순으로 정렬하고
if ans2:                                # ans2에 선별한 소의 합이 있다면
    print(*ans2)                        # 출력하고
else:                                   # 선별한 소의 합이 없다면
    print(-1)                           # -1을 출력한다