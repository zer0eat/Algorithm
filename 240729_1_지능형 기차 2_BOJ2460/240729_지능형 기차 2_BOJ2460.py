# 지능형 기차 2_BOJ2460

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                 # 정답을 저장할 변수를 생성하고
tmp = 0                                 # 현재 인원을 저장할 변수를 생성한다
for n in range(10):                     # 10개의 역을 반복해서
    a, b = map(int, input().split())    # 내린사람과 탄사람의 수를 input 받고
    tmp += b                            # tmp에 탄사람을 더하고
    tmp -= a                            # tmp에 내린사람을 빼서
    ans = max(ans, tmp)                 # ans와 tmp 중 최대 값을 저장한다
print(ans)                              # 기차에 가장 많이 탄 인원을 출력한다