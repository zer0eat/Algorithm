# Animal King Election_BOJ17598

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L, T = 0, 0                     # 사자와 호랑이의 수를 input 받고
for n in range(9):              # 9마리의 동물을 반복해서
    animal = input().strip()    # 동물을 input 받고
    if 'Lion' == animal:        # 사자라면
        L += 1                  # L에 추가하고
    else:                       # 호랑이라면 
        T += 1                  # T에 추가해서
if L > T:                       # 사자가 더 많으면
    print('Lion')               # 사자를 출력하고
else:                           # 그렇지 않으면
    print('Tiger')              # 호랑이를 출력한다