# 단어 뒤집기_BOJ9093

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 문장의 수를 input 받고
for n in range(N):                          # 문장의 수를 반복해서
    word = list(input().split())            # 문장을 리스트로 input 받고
    for w in word:                          # 단어별로 반복해서
        for i in range(len(w)-1, -1, -1):   # 단어를 뒤에서부터 반복해서
            print(w[i], end='')             # 알파벳을 출력하고
        else:                               # 단어가 끝나면
            print(' ', end='')              # 띄어쓰기를 한다
    else:                                   # 문장이 끝났을 때
        if n != N-1:                        # 마지막 문장이 아니라면
            print()                         # 줄을 바꾼다