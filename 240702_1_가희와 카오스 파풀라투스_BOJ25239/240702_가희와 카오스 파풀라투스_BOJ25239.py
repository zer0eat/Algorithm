# 가희와 카오스 파풀라투스_BOJ25239

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
h, m = map(int, input().split(':'))                 # 시와 분을 input 받고
N = list(map(int, input().split()))                 # 영역 별 체력이 차는 값을 리스트로 input 받는다
L = int(input())                                    # 이벤트의 수를 input 받고
tmp = [1]*6                                         # 영역을 체크할 리스트를 생성하고
for l in range(L):                                  # 이벤트를 반복해서
    s, p = input().split()                          # 초와 아이템을 input 받고
    if float(s) >= 60:                              # 초가 60초 이상이라면
        break                                       # 이벤트를 종료한다
    if p == '^':                                    # 이벤트로 키보드 위쪽을 누른다면
        tmp[h//2] = 0                               # 시침이 있는 부분을 봉인한다
    elif 'MIN' in p:                                # 이벤트로 분을 얻었다면
        p = int(p.replace('MIN', ''))               # 얻은 분을 추출하고
        if p + m < 60:                              # 현재 분에 얻은 분을 더해 60 미만이라면
            m += p                                  # 현재 분에 얻은 분을 더해준다
        else:                                       # 60분 이상이라면
            h, m = (h+1) % 12, (m+p) % 60           # 시침을 1 증가시키고 분침을 계산한다
    else:                                           # 이벤트로 시를 얻었다면
        h = (h + int(p.replace('HOUR', ''))) % 12   # 현재 시간에 얻은 시간을 더해준다
ans = 0                                             # 정답을 저장할 변수를 생성하고
for n in range(6):                                  # 시침의 영역의 반복해서
    if tmp[n]:                                      # 시침의 영역이 막히지 않았다면
        ans += N[n]                                 # 회복되는 체력을 더해준다
if ans <= 100:                                      # 체력이 100 이하라면
    print(ans)                                      # 체력을 출력하고
else:                                               # 체력이 100보다 크다면
    print(100)                                      # 100을 출력한다