# 수열 정렬_BOJ1015

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 배열의 크기를 input 받고
A = list(map(int, input().split())) # 배열의 원소를 리스트로 input 받는다
sorted_A = sorted(A, reverse=True)  # 배열을 내림차순으로 정렬한 리스트를 생성하고
dic = dict()                        # 정렬된 배열의 순서를 저장할 딕셔너리를 생성한다
cnt = N-1                           # 배열의 최대 인덱스를 cnt에 저장하고
for s in sorted_A:                  # 정렬된 배열을 반복해서
    dic[s] = cnt                    # s를 key로 정렬 후 순서를 value로 저장하고
    cnt -= 1                        # 정렬 후 순서를 1 빼준다
ans = []                            # 정렬된 배열의 순서를 저장할 리스트를 생성하고
for a in A:                         # 배열을 반복해서
    ans.append(dic[a])              # a의 정렬 후 순서를 ans에 append하고
    dic[a] += 1                     # a의 순서를 1 추가한다
print(*ans)                         # 비내림차순으로 만든 수열을 출력한다