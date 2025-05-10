# 유학 금지_BOJ2789

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
cambridge = ['C','A','M','B','R','I','D','G','E']   # 캠브릿지 단어를 리스트에 저장하고
word = input().strip()                              # 단어를 input받고
for w in word:                                      # 단어를 반복해서
    if w not in cambridge:                          # 캠브릿지에 포함되지 않은 알파벳이라면
        print(w, end='')                            # 단어를 출력한다