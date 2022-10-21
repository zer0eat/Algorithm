# FourSquares_BOJ17626

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())                               # N 제곱 수의 합으로 구하려는 자연수를 input 받는다

ans = [0]                                                   # 0을 넣은 리스트를 생성하고
i = 1                                                       # 1을 i에 저장하고
while i**2 <= N:                                            # i의 제곱수가 N보다 커질때 까지 반복해서
    ans.append(i**2)                                        # 제곱수를 ans에 append하고
    i += 1                                                  # i에 1을 더한다

for a in range(len(ans)):                                   # 4개 이하의 제곱수의 합으로 모든 자연수를 표현할 수 있으므로 ans를 반복해서
    for b in range(len(ans)):
        for c in range(len(ans)):
            for d in range(len(ans)):
                if ans[a]+ans[b]+ans[c]+ans[d] == N:        # ans에서 추출한 4개의 합이 N일 때
                    cnt = 0                                 # cnt를 생성하고
                    if a != 0:                              # 0이면 제곱수를 더한 값이 아니므로 0이 아닐때만 cnt 1을 추가한다
                        cnt += 1
                    if b != 0:
                        cnt += 1
                    if c != 0:
                        cnt += 1
                    if d != 0:
                        cnt += 1
                    print(cnt)                              # cnt를 출력하고
                    exit()                                  # 종료한다