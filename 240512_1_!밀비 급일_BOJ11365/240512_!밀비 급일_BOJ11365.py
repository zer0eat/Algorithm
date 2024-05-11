# !밀비 급일_BOJ11365

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                    # break가 나올 때까지 반복해서
    word = input().strip()  # 암호를 input 받고
    if word == 'END':       # 암호가 END라면
        break               # while문을 break하고
    print(word[::-1])       # 암호라면 암호문을 뒤집어서 출력한다