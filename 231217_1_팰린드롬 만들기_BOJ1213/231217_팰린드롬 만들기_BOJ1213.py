# 팰린드롬 만들기_BOJ1213

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import Counter

# input 받기
name = list(input().strip())            # 이름을 리스트로 input 받고
name.sort()                             # 스펠링을 오름차순으로 정렬한다
num = Counter(name)                     # 스펠링의 개수를 세서 num에 저장하고
center = ''                             # 알파벳의 수가 홀수개라서 가운데 와야할 알파벳을 저장할 변수를 생성하고
for i in num:                           # 스펠링을 반복해서
    if num[i] % 2:                      # 해당 알파벳이 홀수라면
        center += i                     # center에 알파벳을 추가하고
        if len(center) > 1:             # center에 저장된 알파벳이 2개 이상이라면
            print("I'm Sorry Hansoo")   # I'm Sorry Hansoo를 출력하고
            quit()                      # 종료한다
ans = ''                                # 정답을 저장할 변수를 생성하고
for i in num:                           # 알파벳을 반복해서
    for j in range(num[i]//2):          # 해당 알파벳의 수를 2로 나눈 몫을 반복해서
        ans += i                        # 팰린드롬의 앞에 저장한다
print(ans + center + ans[::-1])         # 반복을 마쳤다면 팰린드롬의 앞부분에 center에 저장된 문자를 붙이고 팰린드롬을 뒤집어 뒤에 붙인 후 출력한다