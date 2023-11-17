# 30_BOJ10610

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()         # 임의의 숫자 N을 input 받고
N = list(map(int, N))       # N의 각 자리 숫자를 리스트의 원소로 바꿔 저장한다
N.sort(reverse=True)        # N을 내림차순으로 정렬하고
if 0 in N:                  # 0이 N에 있다면 30의 배수가 될 수 있으므로 다음을 진행하고
    tmp = 0                 # 각 자리의 합을 저장할 변수를 생성하고
    ans = ''                # 가장 큰수를 저장할 변수를 생성한다
    for i in N:             # N을 반복해서
        tmp += i            # tmp에 각자리 수를 int로 더하고
        ans += str(i)       # ans에 각자리 수를 str로 더한다
    else:                   # 모든 수를 반복했다면
        if tmp % 3:         # tmp가 3의 배수가 아닌 경우에는 30의 배수가 아니므로
            print(-1)       # -1을 출력하고
        else:               # tmp가 3의 배수인 경우에는
            print(ans)      # 가장큰 30의 배수를 출력한다
else:                       # 0이 N에 없다면 30의 배수가 될 수 없으므로
    print(-1)               # -1을 출력한다