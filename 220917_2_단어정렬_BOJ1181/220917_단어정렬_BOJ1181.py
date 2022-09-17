# 단어정렬_BOJ1181

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())            # 정렬할 단어의 개수
ans = []                    # 단어를 저장할 빈 리스트
for n in range(N):          # 단어의 수만큼 반복할 때
    a = input()             # input 받는 단어를 a에 저장
    if a in ans:            # ans에 이미 있는 단어라면 패스
        pass
    else:                   # ans에 없는 단어라면 ans에 저장
        ans.append(a)
ans.sort()                  # 알파벳 순으로 정렬하고
ans.sort(key=len)           # 길이 순으로 정렬해서

for s in ans:               # 하나씩 출력한다
    print(s)




