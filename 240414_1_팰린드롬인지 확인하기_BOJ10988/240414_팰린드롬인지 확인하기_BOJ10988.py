# 팰린드롬인지 확인하기_BOJ10988

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word = input().strip()          # 단어를 input 받고
N = len(word)//2                # 단어의 길이의 절반을 변수에 저장하고
for n in range(N):              # N을 반복해서
    if word[n] != word[-n-1]:   # 앞에서 n번째와 뒤에서 n번째 단어가 같은지 확인해서 다르다면
        print(0)                # 팰린드롬이 아니므로 0을 출력하고
        break                   # for문을 종료한다
else:                           # for문을 모두 돌았다면
    print(1)                    # 팰린드롬이므로 1을 출력한다