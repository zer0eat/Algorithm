# LCS2_BOJ9252

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word1 = input().strip()                 # 첫번째 문자열을 input 받고
word2 = input().strip()                 # 두번째 문자열을 input 받은 후
w1 = len(word1)                         # 첫번째 문자열의 길이를 저장한 변수를 생성하고
w2 = len(word2)                         # 두번째 문자열의 길이를 저장한 변수를 생성하고
lst = [''] * w2                         # 최대길이를 저장할 리스트를 생성한다
for i in range(w1):                     # 첫번째 문자열의 길이만큼 반복해서
    cnt = ''                            # 두번째 문자열을 반복할 때 최대 길이를 저장할 변수를 만들고
    for j in range(w2):                 # 두번째 문자열의 길이 까지 반복해서
        if len(cnt) < len(lst[j]):      # cnt에 저장된 문자열이 j번째까지 저장된 문자열보다 짧다면
            cnt = lst[j]                # cnt에 j번째 문자열을 저장한다
        elif word1[i] == word2[j]:      # 첫번째 문자열의 i번째 단어가 두번째 문자열의 j번째 단어가 같을 때
            lst[j] = cnt + word2[j]     # 저장할 리스트의 j번째 원소에 cnt에 같은 문자를 붙여 저장한다다print(len(max(lst, key=len)))           # 저장된 리스트 중 길이가 가장 긴 길이를 출력하고
print(max(lst, key=len))                # 저장된 리스트 중 길이가 가장 긴 문자열을 출력한다