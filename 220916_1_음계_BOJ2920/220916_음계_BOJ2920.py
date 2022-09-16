# 음계_BOJ2920

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
sound = list(map(int, input().split()))

if sound == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif sound == [8,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')
