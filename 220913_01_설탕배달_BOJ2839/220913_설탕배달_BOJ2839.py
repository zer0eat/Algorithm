# 설탕배달_BOJ2839

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                    # 배달할 설탕의 kg
n = 1                               # 5kg 짜리 설탕의 개수로 사용할 변수
ans = []                            # 5kg 설탕으로 배달할 수 있는 최대 개수를 저장할 리스트
while 1:                            # break가 나올때까지 반복할 때
    if 5 * n <= N:                  # 5kg*n개가 N보다 작을 때
        if (N - 5*n) % 3 == 0:      # N에서 5kg*n 뺀 후 나머지가 3으로 나눠떨어지면 배달 가능하므로
            ans.append(n)           # n을 입력한 뒤
            n += 1                  # n을 하나 증가시킨다
        else:                       # N에서 5kg*n 뺀 후 나머지가 3으로 나눠 떨어지지 않는다면
            n += 1                  # 배달 불가능하므로 n만 증가시킨다
    else:                           # 5kg*n개가 N보다 클 때 반복문 종료
        break
if len(ans) == 0:                   # 5kg으로 배달할 수 있는 경우가 없어 ans가 비어있다면
    if N % 3 == 0:                  # 전부다 3kg으로 배달할 수 있는지 확인하고
        print(N//3)                 # 할 수 있다면 3kg으로 배달할 포대를 출력하고
    else:                           # 이 경우도 불가능 하다면
        print(-1)                   # -1 을 출력한다
else:                               # 5kg으로 배달할 수 있는 경우가 있다면
    A = ans.pop(-1)                 # 5kg 포대를 가장 많이 배달할 수 있는 개수를 A에 저장하고
    B = (N - (5*A))//3              # 3kg으로 배달할 수 있는 것을 B에 저장한 후
    print(A+B)                      # 그 개수를 출력한다