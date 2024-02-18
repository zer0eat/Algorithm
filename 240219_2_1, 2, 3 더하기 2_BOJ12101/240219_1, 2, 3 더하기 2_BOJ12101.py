# 1, 2, 3 더하기 2_BOJ12101

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())    # N 숫자의 합 / K 순열의 순번을 input 받고
lst = [1, 2, 3]                     # 1,2,3 리스트를 생성하고
num = []                            # 합이 N이 되는 중복순열을 저장할 리스트를 생성한다

def recur(dep, tmp):
    if sum(tmp) == N:               # 순열의 합이 N이라면
        num.append(tmp[:])          # num에 순열을 append하고
        return                      # return한다
    elif sum(tmp) > N:              # 순열의 합이 N 초과라면
        return                      # return한다
    for i in lst:                   # 리스트를 반복해서
        tmp.append(i)               # i를 넣고
        recur(dep+1, tmp)           # dep+1 깊이부터 중복순열을 탐색하고
        tmp.pop()                   # i를 뺀다

recur(0, [])                        # 깊이 0 부터 합이 N이 되는 중복순열을 탐색한다 
num.sort()                          # 합이 N이 되는 순열을 오름차순으로 정렬하고
if len(num) < K:                    # 순열의 종류가 K보다 작다면
    print(-1)                       # -1을 출력하고
else:                               # 순열의 종류가 K 이상이라면
    ans = num[K-1]                  # K번째 순열을 ans에 저장하고
    for n in range(len(ans)):       # 순열을 반복해서
        if n == len(ans)-1:         # 마지막 인덱스라면
            print(ans[n])           # 숫자만 출력하고
        else:                       # 마지막 인덱스가 아니라면
            print(ans[n], end='+')  # 숫자와 +를 같이 출력한다