# 그룹단어체커_BOJ1316

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                        # 문자열의 수
ans = 0                                 # 그룹단어의 개수를 저장할 변수
for n in range(N):                      # 문자열의 수만큼 반복할 때
    word = input()                      # word에 단어를 input 받고
    tmp = [word[0]]                     # tmp의 리스트에 word의 첫 단어를 입력한다
    for w in range(1, len(word)):       # word의 단어를 하나씩 반복해서
        if word[w-1] == word[w]:        # 전과 같은 단어가 나오면 패스하고
            pass
        else:                           # 전과 다른 단어가 나오면
            tmp.append(word[w])         # tmp 리스트에 추가한다
    else:                               # 단어를 모두 반복했을 때
        if len(tmp) == len(set(tmp)):   # 리스트 tmp와 set tmp가 같다면
            ans += 1                    # 그룹단어이므로 ans에 1을 추가하고
        else:                           # 다르다면 같은 단어가 뒤에 다시 등장 한것이므로
            pass                        # 패스한다
print(ans)

