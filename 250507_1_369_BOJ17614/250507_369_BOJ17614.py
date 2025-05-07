# 369_BOJ17614

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 숫자를 input 받고
ans = 0                         # 정답을 저장할 변수를 생성해서
for n in range(1, N+1):         # 1부터 N까지 반복해서
    tmp = list(str(n))          # 숫자를 리스트에 저장하고
    for t in tmp:               # 각 자리 수를 반복해서
        if t in ['3','6','9']:  # 3, 6, 9가 들어있다면
            ans += 1            # 정답에 1을 추가하고
print(ans)                      # 박수 친 횟수를 출력한다