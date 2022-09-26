# 펠린드롬수_BOJ1259

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                                                    # break까지 반복할 때
    arr = list(input())                                                     # 회문인지 검사할 문장을 arr에 input
    if arr == ['0']:                                                        # 0만 input 받았다면 break
        break                                                   
    if len(arr) % 2 == 1:                                                   # arr의 길이가 홀수 일 때
        if arr[:len(arr)//2] == arr[len(arr) - 1 : len(arr)//2 : -1]:       # 가운데를 뺀 양쪽이 대칭이면 yes를 출력
            print('yes')
        else:                                                               # 아니라면 no를 출력
            print('no')                                         
    elif len(arr) % 2 == 0:                                                 # arr의 길이가 짝수 일 때
        if arr[:len(arr)//2] == arr[len(arr) - 1 : len(arr)//2 -1: -1]:     # 양쪽이 대칭이면 yes를 출력
            print('yes')
        else:                                                               # 아니라면 no를 출력
            print('no')