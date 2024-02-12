# Sleeping in Class_BOJ24620

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # 수업의 횟수를 input 받고
    A  = list(map(int, input().split()))    # 수업시간 별 잠든 횟수를 리스트로 input 받는다
    M = max(A)                              # 가장 많이 잠든 횟수를 저장한 변수를 생성하고
    sumA = sum(A)                           # 총 합을 저장한 변수를 생성한다
    for n in range(N, 0, -1):               # 수업 횟수를 내림차순으로 반복해서 
        if sumA%n == 0 and sumA//n >= M:    # 전체 잠든횟수가 n번의 수업시간으로 나누어 떨어지고, n번으로 나눴을 때 잠든 횟수가 M 이상일 때
            ans = 0                         # 정답을 저장할 변수를 생성하고
            tmp = 0                         # 잠든 횟수를 저장할 변수를 생성한다
            for a in A:                     # 수업 별 잠든 횟수를 반복해서
                tmp += a                    # tmp에 잠든 횟수를 더하고
                if tmp == sumA//n:          # 잠든 횟수가 sumA//n와 같다면
                    tmp = 0                 # tmp를 초기화한다
                elif tmp > sumA//n:         # 잠든 횟수가 sumA//n를 초과한다면
                    break                   # 로그를 sumA//n으로 만들 수 없으므로 for문을 break한다
                else:                       # 잠든 횟수가 sumA//n 미만이라면
                    ans += 1                # 로그를 합칠 횟수를 1개 추가한다
            else:                           # for문을 모두 통과했다면 sumA//n으로 로그를 합칠 수 있으므로
                print(ans)                  # 합친 횟수를 출력하고
                break                       # for문을 break한다