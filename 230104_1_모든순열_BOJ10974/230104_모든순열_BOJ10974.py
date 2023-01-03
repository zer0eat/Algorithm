# 모든순열_BOJ10974

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def permutation(A):
    if A == N:                              # A가 N이 되었을 때
        ans.append(lst[:])                  # lst를 ans에 append 한다
    for a in range(A, N):                   # A부터 N-1까지 반복해서
        lst[a], lst[A] = lst[A], lst[a]     # a번째 요소와 A번째 요소를 바꾸고
        permutation(A+1)                    # 다음 인덱스를 살펴보고
        lst[a], lst[A] = lst[A], lst[a]     # a번째 요소와 A번째 요소를 다시 제자리로 바꿔 놓는다

# input 받기
N = int(sys.stdin.readline().strip())       # 리스트의 최대 값
lst = [_ for _ in range(1,N+1)]             # 1부터 N까지 요소를 갖는 리스트를 생성한다
ans = []                                    # 정답을 저장할 빈 리스트를 생성하고
permutation(0)                              # permutation 함수를 0번째 요소부터 돌린 후
ans.sort()                                  # ans를 오름차순 정렬한다

for a in ans:                               # ans를 반복해서
    print(*a)                               # 요소를 출력한다