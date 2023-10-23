# 시험감독_BOJ13458

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 시험장의 개수를 input 받고
A = list(map(int, input().split()))     # 각 시험장의 응시자 수를 list로 input 받는다
B, C = map(int, input().split())        # B 총감독관의 감시인원 수 / C 부감독관의 감시인원 수를 input 받고
ans = 0                                 # 정답을 저장할 변수를 생성한다
for a in A:                             # 각 시험장을 반복해서
    ans += 1                            # ans에 총감독관의 수를 더하고
    a -= B                              # 시험장의 인원에서 총감독관의 감시인원을 뺀 후
    if a > 0:                           # 감시할 응시자가 남아 있다면
        if a % C:                       # 부감독관의 감시인원수로 나누어 떨어지지 않으면떨어지면
            ans += (a // C) + 1         # ans에 남은 감시인원을 부감독관의 감시인원 수로 나눈 몫과 추가로 1을 더한다
        else:                           # 부감독관의 감시인원수로 나누어 떨어지면
            ans += (a // C)             # ans에 남은 감시인원을 부감독관의 감시인원 수로 나눈 몫을 더한다
print(ans)                              # 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력한다