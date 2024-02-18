# 로또_BOJ6603

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def recur(dep, start, ans):
    if dep == 6:                            # 6개의 로또번호를 골랐다면
        print(*ans)                         # 출력하고
        return                              # 리턴한다
    for i in range(start, N):               # start 인덱스부터 반복해서
        ans.append(lst[i])                  # i번째 번호를 append하고
        recur(dep+1, i+1, ans)              # 깊이 dep+1, i+1 인덱스부터 탐색을 시작해서 로또번호를 탐색하고
        ans.pop()                           # i번째 번호를 pop한다

while 1:
    lst = list(map(int, input().split()))   # 로또의 수와 숫자를 리스트로 input 받고
    if lst == [0]:                          # 로또의 수가 0이면
        break                               # while문을 break한다
    else:                                   # 로또의 수가 0이 아니면
        N = lst[0]                          # 로또의 수를 N에 저장하고
        lst[:1] = []                        # 로또 번호만 lst에 저장한다
        recur(0, 0, [])                     # 깊이 0, 0 인덱스부터 탐색을 시작해서 로또번호를 탐색한다
        print()                             # 로또 번호를 출력한 후 빈 줄을 추가한다