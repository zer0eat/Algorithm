# 줄 세우기_BOJ1681

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, L = map(int, input().split())    # 숫자의 개수와 포함되면 안되는 숫자를 Input받고
L = str(L)                          # 숫자를 문자로 변경해서
ans = []                            # 숫자를 저장할 리스트를 생성하고
tmp = 1                             # 현재 숫자를 표시할 변수를 생성한다 
while len(ans) < N:                 # 저장된 숫자가 N개가 될때까지 반복해서
    if L not in str(tmp):           # L이 포함되지 않은 숫자라면
        ans.append(tmp)             # 리스트에 append하고
    tmp += 1                        # 다음 숫자로 넘어간다
print(ans[-1])                      # 가장 큰 숫자를 출력한다