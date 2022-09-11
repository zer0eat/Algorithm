# 단어공부_BOJ1157

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
arr = input()                                       # 문자열 받기
ans = [0]*26                                        # 각각의 문자 개수를 저장할 빈 리스트 만들기
for a in arr:                                       # 문자열을 반복해서
    if 65 <= ord(a) <= 90:                          # 대문자가 나오면
        ans[ord(a) - 65] += 1                       # A-Z까지 0-25 인덱스에 나온 개수를 추가한다
    elif 97 <= ord(a) <= 122:                       # 소문자가 나오면
        ans[ord(a) - 97] += 1                       # a-z까지 0-25 인덱스에 나온 개수를 추가한다
maxi = 0                                            # 최대값을 저장한 변수와
maxans = []                                         # 최대값을 저장할 빈리스트를 생성 후
for s in ans:                                       # ans를 반복하여
    if s > maxi:                                    # maxi보다 큰 숫자가 나오면
        maxans = []                                 # maxans 리스트를 비운후
        maxi = s                                    # maxi에 s 를 저장하고
        maxans.append(s)                            # maxans에 maxi를 append
    elif s == maxi:                                 # maxi와 같은 숫자가 나오면
        maxans.append(s)                            # maxans에 maxi를 append
else:                                               # 반복이 끝났을 때
    if len(maxans) == 1:                            # maxans가 1이면
        print(chr(ans.index(max(ans)) + 65))        # 가장 많은 문자를 대문자로 출력하고
    else:                                           # 그렇지 않으면
        print('?')                                  # ?를 출력한다