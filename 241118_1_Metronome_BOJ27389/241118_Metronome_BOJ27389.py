# Metronome_BOJ27389

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 노래의 길이를 input 받고
print(N/4)          # 키를 돌려야할 바퀴수를 출력한다