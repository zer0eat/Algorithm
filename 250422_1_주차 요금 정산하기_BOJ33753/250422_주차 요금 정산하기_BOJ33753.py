# 주차 요금 정산하기_BOJ33753

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B, C = map(int, input().split()) # 기본 주차비 초과시간 시간 당 비용을 input받고
T = int(input())                    # 주차시간을 input 받고
if T != 0:                          # 주차를 했다면
    ans = A                         # 기본주차료를 정답을 저장할 변수를 생성해서
else:                               # 주차를 안했다면
    ans = 0                         # 0원을 출력하고
    quit()                          # 종료한다
T -= 30                             # 기본시간을 빼주고
if T > 0:                           # 기본시간 초과해서 주차했다면
    ans += (T+B-1)//B*C             # 시간당 초과 비용을 추가하고
print(ans)                          # 주차비용을 출력한다