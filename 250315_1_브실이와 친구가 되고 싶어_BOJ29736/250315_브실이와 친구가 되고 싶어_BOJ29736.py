# 브실이와 친구가 되고 싶어 🤸‍♀️_BOJ29736

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 푼 문제의 시작과 끝을 input 받고
K, X = map(int, input().split())    # 브실이의 푼 문제와 친구의 범위를 input 받고
ans = 0                             # 정답을 저장할 변수를 생성한다
for a in range(K-X, K+X+1):         # 브실이와 친구가 될수 있는 범위를 반복해서
    if A <= a and a <= B:           # 브실이와 친구가 될 수 있다면
        ans += 1                    # 정답에 추가한다
if ans:                             # 친구가 있다면
    print(ans)                      # 친구의 수를 출력하고
else:                               # 친구가 없다면
    print('IMPOSSIBLE')             # 불가능을 출력한다