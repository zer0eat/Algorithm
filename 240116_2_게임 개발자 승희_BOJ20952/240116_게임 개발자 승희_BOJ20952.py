# 게임 개발자 승희_BOJ20952

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())            # N 수열 A의 길이 / M 수열 B의 길이를 input 받고
A = list(map(int, input().split()))         # 수열 A를 리스트로 input 받고
B = list(map(int, input().split()))         # 수열 B를 리스트로 input 받는다
mod = 1000000007                            # 답이 커졌을 때 줄이기 위한 나머지 연산의 수를 mod에 저장하고
visited = [0] * 7                           # 7로 나눈 나머지를 저장할 리스트를 생성한다
cnt = 0                                     # 7로 나눈 나머지 종류의 수를 저장할 변수를 생성하고
for n in range(N):                          # A 리스트를 반복해서
    if visited[A[n] % 7] == 0:              # n번째 원소를 7로 나눈 나머지가 처음나왔다면
        visited[A[n] % 7] = 1               # 해당 인덱스를 1로 표시해주고
        cnt += 1                            # 7로 나눈 나머지 종류의 수를 1 추가한다
    if cnt == 7:                            # 모든 종류의 나머지가 나왔다면
        break                               # for문을 종료한다
sumB = 0                                    # B를 더한 후 나머지를 저장할 변수를 생성하고
total = 0                                   # B를 모두 더한 수를 저장할 변수를 생성한 후
for m in range(M):                          # B 리스트를 반복해서
    if (sumB + B[m]) % 7 != 0:              # 현재까지의 나머지에 m번째 원소를 더한후 7로 나눈 나머지가 0이 아니면
        tmp = 7 - (sumB + B[m]) % 7         # 7에서 (sumB + B[m]) % 7를 뺀 인덱스가 7로 나누어 떨어지므로 tmp에 저장하고
    else:                                   # 현재까지의 나머지에 m번째 원소를 더한후 7로 나눈 나머지가 0이라면
        tmp = 0                             # 0번째 인덱스가 7로 나누어 떨어지므로 tmp에 저장한다
    if visited[tmp]:                        # tmp 인덱스의 visited가 남아있을 때
        if cnt == 1:                        # 마지막 남아 있는 원소라면
            continue                        # 해당원소는 제거하지 않고 건너 뛰고
        visited[tmp] = 0                    # tmp에 해당 되는 원소를 0으로 표시하여 제거하고
        cnt -= 1                            # 7로 나눈 나머지 종류를 1 제거한다
    sumB = (sumB + B[m]) % 7                # 현재까지의 합을 7로 나눈 나머지를 sumB에 저장하고
    total += B[m]                           # m번째 원소를 전체 합에 더하고
    total %= mod                            # mod로 나눈 나머지만 저장한다
ans = []                                    # 정답을 저장할 리스트를 생성하고
for n in range(N):                          # A 리스트를 반복해서
    if visited[A[n] % 7]:                   # n번째 원소가 제거되지 않았다면
        ans.append((A[n]+total) % mod)      # 연산 후 값을 ans에 추가한다
print(len(ans))                             # 연산을 수행한 후 수열 A의 길이를 출력하고
print(*ans)                                 # 연산을 수행한 후 수열 A의 원소를 출력한다