# 가희와 클럽 오디션 1_BOJ30794

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
lv = list(input().split())  # 콤보와 상태를 input 받고
if lv[1] == 'miss':         # miss 상태라면
    print(int(lv[0])*0)     # 콤보에 0을 곱한 수를 출력하고
elif lv[1] == 'bad':        # bad 상태라면
    print(int(lv[0])*200)   # 콤보에 200을 곱한 수를 출력하고
elif lv[1] == 'cool':       # cool 상태라면
    print(int(lv[0])*400)   # 콤보에 400을 곱한 수를 출력하고
elif lv[1] == 'great':      # great 상태라면
    print(int(lv[0])*600)   # 콤보에 600을 곱한 수를 출력하고
elif lv[1] == 'perfect':    # perfect 상태라면
    print(int(lv[0])*1000)  # 콤보에 1000을 곱한 수를 출력한다