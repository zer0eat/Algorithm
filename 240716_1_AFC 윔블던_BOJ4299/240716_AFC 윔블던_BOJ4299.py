# AFC 윔블던_BOJ4299

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
s, m = map(int, input().split())        # 두팀 점수의 합과 차를 input 받고
if  s+m < 0 or s-m < 0 or (s + m) % 2:  # 두팀의 점수 주 음수가 있거나 정수가 아니라면
    print(-1)                           # -1을 출력하고
else:                                   # 두팀의 점수의 합과 차가 s, m이 된다면
    a = (s + m) // 2                    # 두 팀중 한 팀의 점수를 구하고
    b = s - a                           # 나머지 팀의 점수를 구해서
    print(max(a, b), min(a, b))         # 점수가 큰팀과 작은팀을 순서대로 출력한다