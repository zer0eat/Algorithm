# 지능형 기차_BOJ2455

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = 0                                 # 정답을 저장할 변수를 생성하고
people = 0                              # 역마다 사람을 셀 변수를 생성한다
for n in range(4):                      # 4개의 역을 반복해서
    a, b = map(int, input().split())    # a 내린사람과 b 탄사람을 input 받고
    people += (b-a)                     # 현재 기차에 탄 사람을 계산하고
    ans = max(ans, people)              # 정답에 기차에 가장 많은 인원이 탔을 때 값을 저장한다
print(ans)                              # 최대 사람 수를 출력한다