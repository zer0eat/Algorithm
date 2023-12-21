# DNA 비밀번호_BOJ12891

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input.txt 열기
S, P = map(int, input().split())        # S DNA 문자열 길이 / P 비밀번호로 사용할 문자열 길이를 input 받고
DNA = input().strip()                   # DNA 문자열을 input 받는다
base = list(map(int, input().split()))  # 비밀번호로 사용할 염기 정보를 input 받고
ans = 0                                 # 비밀번호의 수를 저장할 변수를 생성한다
cnt = [0, 0, 0, 0]                      # 비밀번호로 사용할 염기 정보와 비교하기 위한 리스트를 생성하고
dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}  # 염기를 키로 밸류를 순서대로 생성한 딕셔너리를 만들고
for i in range(P):                      # 비밀번호로 사용할 문자열의 길이만큼 반복해서
    cnt[dic[DNA[i]]] += 1               # 해당 염기와 같은 위치에 염기 개수를 추가한다
for k in range(4):                      # 4개의 염기를 반복해서
    if cnt[k] < base[k]:                # 저장된 염기가 기준 염기보다 적다면
        break                           # for문을 break하고
else:                                   # 4개의 염기 모두 기준 염기보다 많다면
    ans += 1                            # 비밀번호로 사용할 수 있기 때문에 ans에 1을 추가한다
for i in range(S - P):                  # DNA의 길이에서 비밀번호로 사용할 문자열의 길이만큼 뺀 수를 반복해서
    cnt[dic[DNA[i]]] -= 1               # 맨 앞의 염기를 제거하고
    cnt[dic[DNA[i+P]]] += 1             # 맨 뒤의 염기를 추가한 후
    for k in range(4):                  # 4개의 염기를 반복해서
        if cnt[k] < base[k]:            # 저장된 염기가 기준 염기보다 적다면
            break                       # for문을 break하고
    else:                               # 4개의 염기 모두 기준 염기보다 많다면
        ans += 1                        # 비밀번호로 사용할 수 있기 때문에 ans에 1을 추가한다
print(ans)                              # 만들 수 있는 비밀번호의 종류의 수를 출력한다