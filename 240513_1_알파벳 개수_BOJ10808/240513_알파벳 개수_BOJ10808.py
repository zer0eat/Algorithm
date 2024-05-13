# 알파벳 개수_BOJ10808

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
ans = [0]*26            # 정답을 저장할 리스트를 생성하고
word = input().strip()  # 단어를 input 받는다
for w in word:          # 단어의 알파벳을 반복해서
    ans[ord(w)-97] += 1 # 해당 알파벳의 개수를 1 추가한다
print(*ans)             # 단어에 포함되어 있는 알파벳의 개수를 출력한다