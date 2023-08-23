# 회사에 있는 사람_BOJ7785

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 출입 기록의 수를 input 받고
lst = {}                        # 딕셔너리를 생성한다
for i in range(N):              # 출입 기록의 수를 반복해서
    name, Q = input().split()   # 이름과 출입기록을 input 받는다
    if Q == 'enter':            # 출입기록이 enter라면
        lst[name] = 1           # 딕셔너리의 키를 name 출입기록을 1로 저장한다
    elif Q == 'leave':          # 출입기록이 leave라면
        lst[name] = 0           # 딕셔너리의 키를 name 출입기록을 0으로 저장한다
ans = []                        # 정답을 저장할 리스트를 생성하고
for l in lst:                   # 딕셔너리의 키를 반복해서
    if lst[l] == 1:             # 해당 키의 밸류가 1이라면
        ans.append(l)           # ans에 이름을 저장한다
ans.sort(reverse=True)          # ans를 내림차순으로 정렬하고
for a in ans:                   # ans를 반복해서
    print(a)                    # 회사에 있는 사람의 이름을 출력한다