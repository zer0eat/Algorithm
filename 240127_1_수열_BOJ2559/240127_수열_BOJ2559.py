# 수열_BOJ2559

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())        # N 정수의 개수 / K 연속적인 날짜를 input 받고
temp = list(map(int, input().split()))  # 온도를 리스트로 input 받고
ans = sum(temp[:K])                     # K일 연속 온도의 합을 ans에 저장하고
sumN = sum(temp[:K])                    # K일 연속 온도의 합을 sumN에 저장한다
for k in range(N-K):                    # N-K일을 반복해서
    sumN -= temp[k]                     # k일의 온도를 빼주고
    sumN += temp[k+K]                   # k+K일의 온도를 더해준 후
    ans = max(ans, sumN)                # 온도의 합이 더 큰값을 ans에 저장한다
print(ans)                              # 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다