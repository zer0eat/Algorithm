# 비슷한 단어_BOJ2607

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 단어의 개수를 input 받고
ans = 0                                     # 정답의 수를 저장할 변수 생성
word = list(input().strip())                # 원본 단어를 list형태로 input 받고

for i in range(1, N):                       # 나머지 단어를 반복해서
    cnt = 0                                 # 서로 다른 개수를 셀 변수를 생성하고
    word1 = word[:]                         # 원본 단어를 word1에 복사하고
    word2 = input().strip()                 # 비교할 단어를 word2에 input 받는다
    for w in word2:                         # 비교할 단어를 반복해서
        if w in word1:                      # 해당 알파벳이 word1에 있다면
            word1.remove(w)                 # word1에서 해당 알파벳을 제거하고
        else:                               # 만약 해당 알파벳이 없다면
            cnt += 1                        # 서로 다른 개수를 1 추가한다
    else:                                   # 모든 반복을 마치고
        if cnt < 2 and len(word1) < 2:      # 서로다른 개수가 2개 미만이면서 남아있는 단어가 2개 미만이면
            ans += 1                        # 정답을 1 추가한다
print(ans)                                  # 비슷한 단어의 수를 출력한다