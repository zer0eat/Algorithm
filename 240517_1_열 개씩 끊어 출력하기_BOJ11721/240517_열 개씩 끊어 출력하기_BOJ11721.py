# 열 개씩 끊어 출력하기_BOJ11721

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = input().strip()              # 출력할 단어를 input 받고
N = len(word)                       # 단어의 길이를 저장한다
for n in range(1, N+1):             # 단어의 길이를 반복해서
    if n % 10 == 0:                 # 해당 철자가 10의 배수의 순서에 나온 철자라면
        print(word[n-1])            # 철자를 출력하고 줄을 바꾸고
    else:                           # 해당 철자가 10의 배수의 순서에 나온 철자가 아니라면
        print(word[n-1], end='')    # 철자를 출력하고 다음 공백을 없앤다