# 명령 프롬프트_BOJ1032

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 단어의 수를 input 받고
word = list(input().strip())    # 첫번째 단어를 input 받는다
for n in range(N-1):            # 나머지 단어를 반복해서
    tmp = list(input().strip()) # 단어를 input 받고
    for t in range(len(word)):  # 단어의 길이를 반복해서
        if word[t] != tmp[t]:   # 두 단어가 서로 다르다면
            word[t] = '?'       # ?로 저장한다
ans = ''                        # 정답을 저장할 변수를 생성하고
for w in word:                  # 단어를 반복해서
    ans += w                    # 스펠링을 저장한 후
print(ans)                      # 패턴을 출력한다