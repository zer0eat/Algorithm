# 로마 숫자 만들기_BOJ16922

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 문자의 수를 input 받고
roma = [1, 5, 10, 50]           # 로마자를 리스트로 생성한 후
ans = set()                     # 정답을 저장할 셋을 생성한다

def recur(dep, start, tmp):
    if dep == N:                # dep이 문자의 수와 같다면
        ans.add(sum(tmp))       # tmp에 담긴 로마자의 합을 ans에 add한 후
        return                  # return한다
    for i in range(start, 4):   # start부터 로마자를 반복해서
        tmp.append(roma[i])     # tmp에 i번째 로마자를 append하고
        recur(dep+1, i, tmp)    # 깊이 dep+1부터 i번 인덱스부터 로마자로 만들 수 있는 수를 탐색한다
        tmp.pop()               # tmp에 i번째 로마자를 pop한다

recur(0, 0, [])                 # 깊이 0부터 0번 인덱스부터 로마자로 만들 수 있는 수를 탐색한다
print(len(ans))                 # 로마 숫자 N개를 사용해서 만들 수 있는 서로 다른 수의 개수를 출력한다