# 영단어 암기는 괴로워_BOJ20920

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                    # N 단어의 개수 / M 단어의 길이
cnt = dict()                                        # 단어가 나온 횟수를 저장할 딕셔너리를 생성하고
for i in range(N):                                  # 단어의 개수만큼 반복해서
    word = input().strip()                          # 나온 단어를 input 받고
    if len(word) >= M:                              # 단어의 길이가 M 이상이라면
        if cnt.get(word) == None:                   # 딕셔너리에 해당 단어가 저장되어 있지 않다면
            cnt[word] = 1                           # 단어를 key로 value가 1인 원소를 생성하고
        else:                                       # 딕셔너리에 해당 단어가 저장되어 있다면
            cnt[word] += 1                          # 단어가 key인 value에 1을 추가한다
ans = []                                            # 외울 단어를 저장할 리스트를 생성하고
for i in cnt:                                       # 딕셔너리의 키를 반복해서
    ans.append([cnt[i], len(i), i])                 # ans 리스트에 [나온 횟수, 단어의 길이, 단어] 정보를 append 한다
ans.sort(key=lambda x:[-x[0], -x[1], x[2]])         # ans 리스트를 자주 나오는 단어 / 길이가 긴 단어 / 사전 순으로 정렬하고
for a in ans:                                       # ans 리스트의 단어를 반복해서
    print(a[2])                                     # 단어장의 단어를 출력한다