# 와글와글 숭고한_BOJ17388

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
s, k, h = map(int, input().split()) # 3 대학의 점수를 input 받고
if s + h + k >= 100:                # 3 대학의 점수의 합이 100점이 넘는다면
    print('OK')                     # OK를 출력하고
else:                               # 100점이 넘지 않는다면
    if s < h:                       # s대가 h대보다 점수가 낮다면
        if s < k:                   # s대가 k대보다 점수가 낮다면
            print('Soongsil')       # 점수가 가장 낮은 Soongsil을 출력한다
        else:                       # s대가 k대보다 점수가 높다면
            print('Korea')          # 점수가 가장 낮은 Korea를 출력한다
    else:                           # s대가 h대보다 점수가 높다면
        if h < k:                   # h대가 k대보다 점수가 낮다면
            print('Hanyang')        # 점수가 가장 낮은 Hanyang를 출력한다
        else:                       # h대가 k대보다 점수가 높다면
            print('Korea')          # 점수가 가장 낮은 Korea를 출력한다