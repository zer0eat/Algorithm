# 파일정리_BOJ20291

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 파일의 수
A = dict()                              # 확장자 파일이 몇개인지 저장할 딕셔너리 생성
for _ in range(N):                      # 파일의 수를 반복해서
    a, b = input().strip().split('.')   # 파일 이름과 확장자 명을 a,b에 input 받고
    if A.get(b) == None:                # 확장자 명을 key로 하는 원소가 없다면
        A[b] = 1                        # 확장자명을 key로 value를 1로 생성하고
    else:                               # 확장자 명을 key로 하는 원소가 있다면
        A[b] += 1                       # 확장자명을 key로 하는 value에 1을 추가한다

ans = []                                # 정답을 저장할 리스트를 생성하고
for a in A:                             # 딕셔너리를 반복해서
    ans.append([a, A[a]])               # ans 리스트에 [확장자, 확장자 파일 수]를 append

ans.sort()                              # ans를 오름차순으로 정렬하고

for a in ans:                           # 정답을 저장할 리스트를 반복해서
    print(*a)                           # 확장자와 파일 수를 출력한다
