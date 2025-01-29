# 핸드폰 요금_BOJ1267

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 전화 수를 input 받고
call = list(map(int, input().split()))  # 전화 시간을 input 받고
young, min = 0, 0                       # 요금을 저장할 변수를 생성한다
for n in range(N):                      # 전화 수를 반복해서
    young += call[n]//30 + 1            # 영식 요금제의 부가량을 더해주고
    min += call[n]//60 + 1              # 민식 요금제의 부가량을 더해주고
if young*10 < min*15:                   # 영식 요금제가 저렴하다면
    print('Y', young*10)                # Y와 비용을 출력하고
elif young*10 > min*15:                 # 민식 요금제가 저렴하다면
    print('M', min*15)                  # M과 비용을 출력하고
else:                                   # 비용이 같다면
    print('Y M', young*10)              # Y M과 비용을 출력한다