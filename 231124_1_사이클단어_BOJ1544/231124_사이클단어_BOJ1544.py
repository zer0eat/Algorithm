# 사이클단어_BOJ1544

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 단어의 개수를 input 받고
ans = []                                        # 정답을 저장할 리스트를 생성한다
for i in range(N):                              # 단어의 개수만큼 반복해서
    word = input().strip()                      # 단어를 input 받고
    flag = False                                # flag를 False로 생성한다
    for a in ans:                               # 정답에 저장된 단어를 반복해서
        if len(a) == len(word):                 # 저장된 단어와 input 받은 단어의 길이가 같다면
            for i in range(len(a)):             # 단어의 길이를 반복해서
                if word[0] == a[i]:             # input받은 단어의 첫글자와 같은 부분이 있다면
                    cnt = i                     # cnt를 해당 인덱스로 저장하고
                    for j in range(len(a)):     # 단어의 길이를 반복해서
                        if word[j] == a[cnt]:   # input받은 단어와 저장된 단어의 스펠링이 일치한다면
                            cnt += 1            # 인덱스를 1추가하고
                            cnt %= len(a)       # 단어의 길이로 나눈 나머지로 인덱스를 저장한다
                        else:                   # 만약 스펠링이 일치하지 않는다면
                            break               # for문을 break한다
                    else:                       # 단어가 완벽히 일치한다면
                        flag = True             # flag를 True로 변경하고
    if flag == False:                           # 저장된 단어와 같은 단어가 없어 flag가 False인 경우
        ans.append(word)                        # input 받은 단어를 ans에 append한다
print(len(ans))                                 # 다른 단어의 개수를 출력한다