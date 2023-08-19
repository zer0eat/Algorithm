# 서로 다른 부분 문자열의 개수_BOJ11478

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = input().strip()                  # 문자열을 input 받고
ans = set()                             # 정답을 저장할 셋을 생성하고
for i in range(len(word)):              # 문자열의 처음을 반복하고
    for j in range(i+1, len(word)+1):   # 문자열의 끝을 반복해서
        ans.add(word[i:j])              # 슬라이스한 문자열을 ans에 add한다
print(len(ans))                         # 문자열의 서로 다른 부분의 개수를 출력한다
