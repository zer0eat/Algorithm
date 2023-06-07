# 두배열의합_BOJ2143

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 부 배열의 합이 되는 수
N = int(input())                            # A 배열의 원소의 수
A = list(map(int, input().split()))         # A 배열을 리스트로 input
M = int(input())                            # B 배열의 원소의 수
B = list(map(int, input().split()))         # B 배열을 리스트로 input

tmp1 = []                                   # A의 부집합의 합을 저장할 리스트 생성
tmp2 = []                                   # B의 부집합의 합을 저장할 리스트 생성

for i in range(N):                          # A배열을 반복해서
    for j in range(i+1, N+1):               # i번째 원소부터 A배열의 끝까지 반복해서
        tmp1.append(sum(A[i:j]))            # i부터 j까지의 합을 tmp1에 append
tmp1.sort()                                 # tmp1을 오름차순으로 정렬한다

for i in range(M):                          # B배열을 반복해서
    for j in range(i+1, M+1):               # i번째 원소부터 B배열의 끝까지 반복해서
        tmp2.append(sum(B[i:j]))            # i부터 j까지의 합을 tmp2에 append
tmp2.sort(reverse=True)                     # tmp2을 오름차순으로 정렬한다

tp1 = 0                                     # tmp1의 포인터 변수 생성
tp2 = 0                                     # tmp2의 포인터 변수 생성
ans = 0                                     # 정답을 저장할 변수 생성
while tp1 < len(tmp1) and tp2 < len(tmp2):  # t1의 포인터와 t2의 포인터가 모두 해당 부집합의 합 리스트보다 커질 때까지 반복해서
    if tmp1[tp1] + tmp2[tp2] == T:          # 두 부집합의 합이 T라면
        ans1 = 1                            # tmp1[t1]과 같은 원소의 개수를 저장할 변수 생성
        for i in range(tp1+1, len(tmp1)):   # t1포인터 부터 tmp1 끝까지 반복해서
            if tmp1[tp1] == tmp1[i]:        # tmp1[t1]와 같은 원소가 나오면
                ans1 += 1                   # ans1에 1을 추가한다
            else:                           # tmp1[t1]와 다른 원소가 나오면
                break                       # for문을 break
        ans2 = 1                            # tmp2[t2]과 같은 원소의 개수를 저장할 변수 생성
        for i in range(tp2+1, len(tmp2)):   # t2포인터 부터 tmp2 끝까지 반복해서
            if tmp2[tp2] == tmp2[i]:        # tmp2[t2]와 같은 원소가 나오면
                ans2 += 1                   # ans2에 1을 추가한다
            else:                           # tmp2[t2]와 다른 원소가 나오면
                break                       # for문을 break
        ans += (ans1 * ans2)                # ans에 부분집합의 수인 ans1 * ans2를 더해준다
        tp1 += ans1                         # t1 포인터를 ans1만큼 이동한다
        tp2 += ans2                         # t2 포인터를 ans2만큼 이동한다
    elif tmp1[tp1] + tmp2[tp2] < T:         # 두 부분집합의 합이 T보다 작다면
        tp1 += 1                            # tmp1의 포인터를 한 칸 이동한다
    elif tmp1[tp1] + tmp2[tp2] > T:         # 두 부분집합의 합이 T보다 크다면
        tp2 += 1                            # tmp2의 포인터를 한 칸 이동한다
print(ans)                                  # 부집합의 개수를 출력한다
