# 수들의 합 4_BOJ2015

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N 수열의 길이 / K 부분합의 합을 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
dic = dict()                            # 부분합을 저장할 딕셔너리를 생성하고
dic[0] = 1                              # 부분합이 0이 되는 것을 1로 저장한다
sumN = 0                                # 리스트의 합을 저장할 변수를 생성하고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for i in range(N):                      # 수열의 길이를 반복해서
    sumN += lst[i]                      # sumN에 i번째 원소를 더하고
    if dic.get(sumN-K):                 # 부분합에서 K만큼 뺀 경우가 있다면
        ans += dic[sumN-K]              # 정답에 그 수를 더해주고
    if dic.get(sumN):                   # 부분합의 경우가 있다면
        dic[sumN] += 1                  # 경우를 1 추가하고
    else:                               # 부분합의 경우가 없다면
        dic[sumN] = 1                   # 경우를 1로 생성한다
print(ans)                              # 합이 K인 부분합의 개수를 출력한다