# 나눌 수 있는 부분 수열_BOJ3673

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
C = int(input())                            # 테스트 케이스를 input 받고
for c in range(C):                          # 테스트 케이스를 반복해서
    D, N = map(int, input().split())        # D 나눠야하는 수 / N 수열의 길이를 input 받는다
    lst = list(map(int, input().split()))   # 수열을 리스트로 input 받고
    ans = 0                                 # 정답을 저장할 변수를 생성하고
    sumN = 0                                # 부분합을 저장할 변수를 생성한 후
    mod = [0]*D                             # 부분합의 나머지를 저장할 리스트를 생성한다
    for i in range(N):                      # 수열을 반복해서
        sumN = (sumN+lst[i]) % D            # 현재까지 수열의 합에 i번째 원소를 더한 값의 나머지를 sumN에 저장한 후
        ans += mod[sumN]                    # 나머지가 sumN인 부분합만큼 정답에 더해주고
        mod[sumN] += 1                      # 나머지가 sumnN인 수를 1 추가시켜준다
        if sumN == 0:                       # 부분합의 나머지가 0이 되었다면
            ans += 1                        # 정답을 1 추가해준다
    print(ans)                              # 연속하는 부분 수열의 합이 d로 나누어 떨어지는 것의 개수를 출력한다