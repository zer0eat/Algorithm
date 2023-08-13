# 암호 만들기_BOJ1759

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

# input 받기
L, C = map(int, input().split())                # L 암호의 길이 / C 암호에 사용한 문자의 수
lst = list(input().split())                     # 암호에 사용한 문자를 리스트로 input 받고
lst.sort()                                      # 암호에 사용한 문자를 오름차순으로 정렬한다
for i in combinations(lst, L):                  # 암호에 사용한 문자열을 L가지 조합으로 만들어서
    ans = ''                                    # 정답을 저장할 변수를 생성하고
    vowels = 0                                  # 모음의 개수를 저장할 변수를 생성하고
    consonant = 0                               # 자음의 개수를 저장할 변수를 생성한다
    for j in i:                                 # 만들어진 암호를 반복해서
        ans += j                                # ans에 암호를 하나 저장하고
        if j in ['a', 'e', 'i', 'o', 'u']:      # 암호가 모음에 포함된다면
            vowels += 1                         # 모음에 1 추가하고
        else:                                   # 그렇지 않다면
            consonant += 1                      # 자음에 1 추가한다
    else:                                       # 만들어진 암호를 모두 확인한 후
        if vowels >= 1 and consonant >= 2:      # 모음이 1개 이상이고 자음이 2개 이상이면
            print(ans)                          # 만들어진 암호를 출력한다