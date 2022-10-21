#_2xn타일링_BOJ11726

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())           # N 가로의 길이

ans = [0, 1, 2]                         # 가로의 길이가 0,1,2 일때 직사각형을 넣을 수 있는 경우의 수를 넣은 리스트 생성

for i in range(3, N+1):                 # 3부터 N까지 반복해서
    ans.append(ans[i - 1] + ans[i - 2]) # i보다 1 작은 숫자의 경우의 수와 2 작은 숫자의 경우의 수의 합이 i의 경우의 수가 되며, 이를 append 한다

print(ans[N] % 10007)                   # N의 경우의 수를 10007로 나눈 나머지를 출력한다
