# 동일한 단어 그룹화하기_BOJ16499

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 단어의 개수를 input 받고
word = []                       # 단어를 저장할 리스트를 생성한다
for n in range(N):              # 단어의 개수를 반복해서
    tmp = list(input().strip()) # 단어를 리스트로 input 받고
    tmp.sort()                  # 단어의 알파벳을 오름차순으로 정렬한 후
    if tmp not in word:         # word 리스트에 같은 단어가 없다면
        word.append(tmp)        # word 리스트에 단어를 append한다
print(len(word))                # 단어 그룹의 최소 숫자를 출력한다