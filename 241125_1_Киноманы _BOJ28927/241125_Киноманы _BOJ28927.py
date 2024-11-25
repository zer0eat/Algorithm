# Киноманы _BOJ28927

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x1, x2, x3 = map(int, input().split())  # Max의 시청한 동영상을 input 받고
Max = x1*3 + x2*20 + x3*120             # Max의 시청시간을 저장한다
e1, e2, e3 = map(int, input().split())  # Mel의 시청한 동영상을 input 받고
Mel = e1*3 + e2*20 + e3*120             # Mel의 시청시간을 저장한다
if Max > Mel:                           # Max가 시청 시간이 더 길면
    print('Max')                        # Max를 출력하고
elif Max < Mel:                         # Mel이 시청 시간이 더 길면
    print('Mel')                        # Mel을 출력하고
else:                                   # 시청 시간이 같으면
    print('Draw')                       # Draw를 출력한다