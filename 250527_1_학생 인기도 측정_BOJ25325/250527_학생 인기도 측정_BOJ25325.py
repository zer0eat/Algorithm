# 학생 인기도 측정_BOJ25325

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 이름의 수를 input받고
name = list(input().split())            # 확인할 이름 리스트를 input받고
dic = {}                                # 횟수를 저장할 딕셔너리를 생성한다
for n in name:                          # 이름 리스트를 반복해서
    dic[n] = 0                          # 이름을 키로 딕셔너리를 생성하고
for n in range(N):                      # 이름의 수를 반복해서
    name = list(input().split())        # 부른 이름 리스트를 input받고
    for n in name:                      # 이름 리스트를 반복해서
        dic[n] += 1                     # 부른 횟수를 추가한다
ans = []                                # 정답을 저장할 리스트를 생성하고
for d, n in dic.items():                # 딕셔너리를 반복해서
    ans.append([n, d])                  # 이름 부른 횟수와 이름을 append하고
ans.sort(key=lambda x: (-x[0], x[1]))   # 부른횟수를 내림차순 이름을 오름차순으로 정렬하고
for a in ans:                           # 이름을 반복해서
    print(a[1], a[0])                   # 이름과 횟수를 출력한다