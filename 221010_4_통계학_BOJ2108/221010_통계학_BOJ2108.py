# 통계학_BOJ2108

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())           # 숫자의 개수
ans = []                                # 숫자를 저장할 리스트 생성
ansd = dict()                           # 숫자를 저장할 딕셔너리 생성
for n in range(N):                      # 숫자의 개수만큼 반복할 때
    a = int(sys.stdin.readline())       # a에 숫자를 input 받고
    ans.append(a)                       # ans에 append 하고
    if ansd.get(a) == None:             # a를 key값으로 하는 value가 없다면
        ansd[a] = 1                     # a를 key로 value가 1인 값을 ansd에 넣어주고
    else:                               # a를 key 값으로 하는 value가 있다면
        ansd[a] += 1                    # value에 1을 추가해준다
ans.sort()                              # ans를 정렬해서

# 산술평균
print(round(sum(ans)/len(ans)))         # 평균을 구해서 반올림한 값을 산술평균으로 출력하고

# 중앙값
print(ans[N//2])                        # 가운데 값을 출력하고

# 최빈값(여러개라면 두번째로 작은수)
many = 0                                # 가장 많은 숫자의 개수를 저장할 변수를 생성하고
manyN = []                              # 가장 많은 숫자를 저장할 리스트를 생성한다
for a in ansd:                          # 딕셔너리를 반복해서
    if ansd.get(a) > many:              # value값이 many보다 많은 경우에
        many = ansd.get(a)              # many에 value값을 저장하고
        manyN = []                      # manyN 리스트를 비운 후
        manyN.append(a)                 # key값을 manyN에 append
    elif ansd.get(a) == many:           # value값이 many와 같은 경우
        manyN.append(a)                 # key값을 manyN에 append
else:                                   # 반복이 끝났다면
    if len(manyN) == 1:                 # manyN의 key 값이 1개이면
        print(*manyN)                   # 출력하고
    else:                               # 1개 이상이면
        manyN.sort()                    # 정렬해서
        print(manyN[1])                 # 두번째로 작은 수를 출력한다

# 범위
print(max(ans)-min(ans))                # 양단의 숫자를 빼서 범위를 출력한다