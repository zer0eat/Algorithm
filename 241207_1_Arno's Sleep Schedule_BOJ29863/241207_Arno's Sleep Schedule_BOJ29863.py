# Arno's Sleep Schedule_BOJ29863

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
sleep = int(input())    # 잠드는 시간을 input 받고
wakeup= int(input())    # 일어나는 시간을 input 받고
ans = wakeup - sleep    # 잠잔 시간을 계산해서
if ans < 0:             # 잠잔시간이 음수라면
    ans += 24           # 24시간을 더해서
print(ans)              # 잠잔시간을 출력한다