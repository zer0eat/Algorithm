# ROT13_BOJ4446

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
mo = ['a', 'i', 'y', 'e', 'o', 'u']                 # 모음 리스트를 저장하고
ja = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']   # 자음 리스트를 저장해서
dic_m = dict()                                      # 모음 딕셔너리를 생성하고
for m in range(len(mo)):                            # 모음의 개수를 반복해서
    dic_m[mo[m]] = m                                # 모음의 순번을 value로 저장한다
dic_j = dict()                                      # 자음 딕셔너리를 생성하고
for j in range(len(ja)):                            # 자음의 개수를 반복해서
    dic_j[ja[j]] = j                                # 자음의 순번을 value로 저장한다
while 1:                                            # break가 나올 때까지 반복해서
    try:                                            # input 있다면
        word = list(input().strip())                # 문장을 input 받고
        flag = False                                # 대문자 표시를 할 변수를 생성한다
        for w in range(len(word)):                  # 문장을 반복해서
            if word[w].isupper():                   # 대문자라면
                flag = True                         # 대문자 표시를 저장하고
                word[w] = word[w].lower()           # 소문자로 변경한다
            if word[w] in mo:                       # w번째 글자가 모음이라면
                tmp = (dic_m[word[w]] + 3) % 6      # 원래 모음으로 순번을 저장하고
                word[w] = mo[tmp]                   # 모음을 변경한다
            elif word[w] in ja:                     # w번째 글자가 자음이라면
                tmp = (dic_j[word[w]] + 10) % 20    # 원래 자음으로 순번을 저장하고
                word[w] = ja[tmp]                   # 자음을 변경한다
            if flag:                                # 대문자 표시가 있다면
                flag = False                        # 대문자 표시를 지우고
                word[w] = word[w].upper()           # 대문자로 변경한다
        ans = ''                                    # 정답을 저장할 변수를 생성하고
        for w in word:                              # 문장을 반복해서
            ans += w                                # 정답에 더해준 후
        print(ans)                                  # ROT13으로 변경 전 문장을 출력한다
    except:                                         # input이 없다면
        break                                       # while문을 break한다