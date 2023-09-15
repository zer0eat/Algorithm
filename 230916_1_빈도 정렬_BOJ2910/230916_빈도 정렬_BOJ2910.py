# 빈도 정렬_BOJ2910

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, C = map(int, input().split())                # N 메세지의 길이 / C 메세지로 들어오는 숫자의 수
lst = list(map(int, input().split()))           # 들어오는 메세지를 리스트로 input받고
ans = dict()                                    # 빈도를 저장할 딕셔너리를 생성한다
for i in range(N):                              # 메세지의 길이를 반복해서
    if ans.get(lst[i]) == None:                 # 들어온 메세지가 등장 전이라면
        ans[lst[i]] = [1, i+1]                  # 들어온 메세지를 key로 value를 [등장횟수, 최초 등장]을 넣고 생성한다
    else:                                       # 들어온 메세지가 등장한 적이 있다면
        ans[lst[i]][0] += 1                     # 등장횟수를 1 추가한다
ans2 = sorted(ans.items(), key=lambda x:(-x[1][0], x[1][1]))    # 등장 횟수를 내림차순 / 최초 등장을 오름차순으로 정렬하고
for a in ans2:                                  # 정렬한 리스트를 반복해서
    for b in range(a[1][0]):                    # 등장한 횟수만큼 반복해서
        print(a[0], end=' ')                    # 해당 메세지의 숫자를 출력한다