# 모음의 개수_BOJ10987

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
moeum = ['a', 'e', 'i', 'o', 'u']   # 모음을 리스트로 저장하고
ans = 0                             # 정답을 저장할 변수를 생성한다
word = list(input().strip())        # 단어를 input 받고
for w in word:                      # 단어를 반복해서
    if w in moeum:                  # 해당 스펠링이 모음이라면
        ans += 1                    # 정답에 1을 더해준다
print(ans)                          # 모음의 개수를 출력한다