# 쿼리 맛보기_BOJ14648

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, Q = map(int, input().split())                # N 수열의 길이와 Q 쿼리의 개수를 input 받고
seq = list(map(int, input().split()))           # 수열을 리스트로 input 받고
for q in range(Q):                              # 쿼리의 개수를 반복해서
    query = list(map(int, input().split()))     # 쿼리를 input 받고
    if query[0] == 1:                           # 쿼리가 1번이라면
        ans = 0                                 # 정답을 저장할 변수를 생성하고
        for n in range(query[1]-1, query[2]):   # 쿼리의 2번째 자리의 수열부터 3번째 자리의 수열까지 반복해서
            ans += seq[n]                       # 수열의 값을 ans에 더한 후
        seq[query[1]-1], seq[query[2]-1] = seq[query[2]-1], seq[query[1]-1] # 쿼리의 2번째와 3번째에 나온 수열의 위치를 바꾼다
    else:                                       # 쿼리가 2번이라면
        ans = 0                                 # 정답을 저장할 변수를 생성하고
        for n in range(query[1]-1, query[2]):   # 쿼리의 2번째 자리의 수열부터 3번째 자리의 수열까지 반복해서
            ans += seq[n]                       # 수열의 값을 ans에 더한 후
        for n in range(query[3]-1, query[4]):   # 쿼리의 4번째 자리의 수열부터 5번째 자리의 수열까지 반복해서
            ans -= seq[n]                       # 수열의 값을 ans에 뺀 후
    print(ans)                                  # 쿼리의 값을 출력한다