# 암호 만들기_BOJ1759

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
L, C = map(int, input().split())                # L 암호의 길이 / C 암호에 들어갈 문자의 수를 input받고
word = list(input().split())                    # 암호에 들어갈 문자를 리스트로 input 받고
word.sort()                                     # 오름차순으로 정렬한다

def recur(dep, start, tmp):
    if dep == L:                                # 깊이가 L이 되면 암호가 완성되므로
        a, b = 0, 0                             # 자음과 모음을 저장할 변수를 생성하고
        for t in tmp:                           # 암호를 반복해서
            if t in ['a', 'e', 'i', 'o', 'u']:  # 암호가 모음이라면
                a += 1                          # a를 추가하고
            else:                               # 암호가 자음이라면
                b += 1                          # b를 추가한다
        if a >= 1 and b >= 2:                   # 모음이 1개 이상 자음이 2개 이상이라면
            print(tmp)                          # 암호를 출력한다
        return                                  # return한다
    for i in range(start, C):                   # start 인덱스부터 반복해서
        recur(dep+1, i+1, tmp+word[i])          # 깊이 dep+1 start 인덱스부터 암호를 탐색한다
   
recur(0, 0, '')                                 # 깊이 0 인덱스 0부터 암호를 탐색한다