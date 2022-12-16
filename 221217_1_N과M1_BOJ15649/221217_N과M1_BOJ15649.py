# N과M1_BOJ15649

# import.txt 열기
import sys
sys.stdin = open('input.txt')

def permutation(n):
    global N, M                                 # 중복 없이 고를 개수를 global로 불러오고
    if n == N:                                  # n이 N과 같아질 때
        ans.add(tuple(lst[0:M]))                # ans에 앞에 M개의 요소를 튜플형태로 add하고
        return                                  # 리턴한다
    for i in range(n,N):                        # 반복문을 n부터 N까지 돌려서
        lst[i], lst[n] = lst[n], lst[i]         # i와 n의 인덱스를 바꾸고
        permutation(n+1)                        # 다음 인덱스로 순열의 조합을 계산하고
        lst[i], lst[n] = lst[n], lst[i]         # i와 n의 인덱스를 제자리로 바꿔 놓는다

# input 받기
N, M = map(int, sys.stdin.readline().split())   # N 수열의 개수 / M 중복 없이 고를 개수

lst = [_ for _ in range(1,N+1)]                 # 1부터 N까지의 수열을 리스트로 생성
ans = set()                                     # 정답을 저장할 set 생성

permutation(0)                                  # permutation 함수를 돌려서

ans = list(ans)                                 # 정답이 저장된 set을 list로 변환한 후
ans.sort()                                      # 오름차순 정렬하고

for a in ans:                                   # 정답을 반복해서
    print(*a)                                   # 하나씩 출력한다



