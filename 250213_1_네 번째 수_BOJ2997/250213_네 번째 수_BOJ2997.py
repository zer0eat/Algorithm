# 네 번째 수_BOJ2997

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
num = list(map(int, input().split()))   # 세 숫자를 input 받고
num.sort()                              # 숫자를 오름차순으로 정렬한다
if num[1]-num[0] == num[2]-num[1]:      # 숫자의 간격이 같다면
    if num[2] + num[1]-num[0] > 100:    # 마지막 숫자가 100 보다 크면
        print(num[0] - num[1]+num[0])   # 맨앞에 같은 간격의 수를 출력하고
    else:                               # 마지막 숫자가 100 이하라면
        print(num[2] + num[1]-num[0])   # 맨뒤에 같은 간격의 수를 출력하고
elif num[1]-num[0] < num[2]-num[1]:     # 3번째 수가 빠졌다면
    print(num[1] + num[1]-num[0])       # 3번째 수를 출력하고
else:                                   # 2번째 수가 빠졌다면
    print(num[0] + num[2]-num[1])       # 2번째 수를 출력한다