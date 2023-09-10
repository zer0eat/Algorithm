# 이름궁합_BOJ15312

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]   # 알파벳의 획수를 리스트로 저장하고
name1 = input().strip()                         # 첫번째 이름을 input받고
name2 = input().strip()                         # 두번째 이름을 input받는다
ans = []                                        # 정답을 저장할 리스트를 생성하고
for i in range(len(name1)):                     # 이름의 길이를 반복해서
    ans.append(alphabet[ord(name1[i])-65])      # 첫번째 이름의 획수를 ans에 append 하고
    ans.append(alphabet[ord(name2[i])-65])      # 두번째 이름의 획수를 ans에 append 하고
while len(ans) > 2:                             # ans의 길이가 2가 될때까지 반복해서
    tmp = []                                    # 궁합을 저장할 리스트를 생성한다
    for a in range(len(ans)-1):                 # ans의 길이보다 1 짧은 수를 반복해서
        tmp.append((ans[a]+ans[a+1])%10)        # a번째 획수와 a+1번째 획수의 합의 일의 자리만 tmp에 append한다
    else:                                       # 모든 반복을 마쳤으면
        ans = tmp[:]                            # ans에 tmp를 저장한다
else:                                           # ans의 길이가 2가 되었으면
    answer = ''                                 # 궁합을 저장할 변수를 생성하고
    for a in ans:                               # 궁합을 반복해서
        answer += str(a)                        # answer에 정답을 더한다
    if len(answer) == 2:                        # answer이 두자리 수라면
        print(answer)                           # answer를 출력하고
    else:                                       # answer이 한자리 수라면
        print('0'+answer)                       # 앞에 0을 붙여 출력한다
