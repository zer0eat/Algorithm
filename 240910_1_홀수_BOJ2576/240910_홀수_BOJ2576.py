# 홀수_BOJ2576

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = []                # 홀수를 저장할 리스트를 생성하고
for n in range(7):      # 7개의 수를 반복해서
    num = int(input())  # 수를 input 받고
    if num % 2:         # input 받은 수가 홀수라면
        ans.append(num) # ans에 append한다
ans.sort()              # ans를 오름차순 정렬하고
if ans:                 # ans에 원소가 있다면
    print(sum(ans))     # 홀수의 합을 출력하고
    print(ans[0])       # 가장 작은 홀수를 출력한다
else:                   # ans에 원소가 없다면
    print(-1)           # -1을 출력한다