# 세로읽기_BOJ10798

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
words = [list(input().strip()) for _ in range(5)]   # 5줄의 단어를 리스트로 input 받고
ans = ''                                            # 정답을 저장할 변수를 생성한다
for i in range(15):                                 # 최대 15개의 원소를 반복해서
    for j in range(5):                              # 5줄의 단어를 반복한다
        if i < len(words[j]):                       # j번째 단어의 길이가 i개 미만이면
            ans += words[j][i]                      # j번째 단어의 i번째 원소를 ans에 더한다
print(ans)                                          # 세로로 읽은 순서대로 글자들을 출력한다