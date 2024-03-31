# 문자열_BOJ1120

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = input().split()              # A와 B 문자열을 input 받고
N = len(A)                          # A의 길이를 저장한 변수를 생성한다
ans = 50                            # 정답을 저장할 변수를 생성하고
for a in range(len(B)-len(A)+1):    # A와 B의 차이만큼 반복하고
    tmp = 0                         # N개의 문자 중 다른 수를 셀 변수를 생성한다
    for n in range(N):              # N개의 문자를 반복해서
        if A[n] != B[a+n]:          # A의 n번째와 B의 a+n번째가 서로 다르다면
            tmp += 1                # tmp에 다른 수를 1 추가한다
    else:                           # 문자를 모두 반복했다면
        ans = min(ans, tmp)         # ans에 더 작은 값을 저장한다
print(ans)                          # A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력한다