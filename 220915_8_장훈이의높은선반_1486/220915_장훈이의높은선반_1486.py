# 장훈이의높은선반_1486

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# 부분 집합으로 탑의 높이 구하기
def height(a):                              # 부분집합의 합을 통해 탑의 높이를 구하는 함수
    global mini                             # 탑의 최소값을 저장할 mini를 불러오고
    # 최소값이 등장하면 함수종료
    if mini == B:                           # 원하는 탑의 높이와 같은 높이가 나와 더이상 최소값이 나올 수가 없는 경우
        return                              # 함수를 종료
    # 부분 집합 완성 후 탑의 높이를 구하기
    if a == N:                              # 모든 요소에 대해 비트를 결정했을 때
        tmp = 0                             # 탑의 높이를 임시 저장할 빈 변수를 만들어주고
        # 부분집합의 요소의 합 구하기
        for q in range(N):                  # 완성된 비트의 부분집합을 반복할 때
            if bit[q] == 1:                 # 비트가 켜져있으면
                tmp += arr[q]               # tmp에 그 요소를 저장한다
            if tmp >= mini:                 # tmp가 최소값을 넘어섰다면
                break                       # 반복문을 break 한다
        # 탑의 높이와 최소값을 비교하기
        else:                               # 부분집합을 모두 돌렸을 때
            if tmp < B:                     # tmp의 값이 최소 탑의 높이보다 작다면
                pass                        # 그 값을 쓸 수 없으므로 패스
            elif tmp == B:                  # tmp가 최소 탑의 높이와 같은 값이 나왔다면
                mini = tmp                  # mini에 최소 높이를 저장하고
                return                      # 이보다 더 낮은 최소값이 나올 수 없으므로 함수를 종료한다
            elif tmp > B:                   # tmp가 최소 탑의 높이 보다 클 경우
                if mini > tmp:              # 현재 저장된 최소 탑의 높이인 mini와 비교해서 그 보다 작다면
                    mini = tmp              # mini에 새로운 최소값을 저장한다
        return                              # 마지막 비트의 함수를 종료한다

    bit[a] = 0                              # 비트를 0으로 저장하고
    height(a+1)                             # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다
    bit[a] = 1                              # 비트를 0으로 부분집합을 구하고 나왔다면 이번에는 비트를 1로 저장하고
    height(a+1)                             # 다음 인덱스의 비트를 결정하기 위한 함수로 들어간다

# input 받기
T = int(input())                            # 테스트 케이스
for t in range(T):                          # 테스트 케이스 반복해서
    N, B = map(int, input().split())        # N = 직원의 숫자 / B = 탑의 최소높이
    arr = list(map(int, input().split()))   # arr에 직원들의 키를 리스트 형태로 받는다

    mini = 200001                           # 직원들이 쌓은 탑의 최소 높이를 저장할 변수를 생성하고
    bit = [0]*N                             # 직원의 수만큼 bit를 생성한다

    height(0)                               # 0부터 부분집합 함수를 돌린 후

    print(f'#{t+1}', mini-B)                # 탑의 최소높이와 요구하는 탑의 높이의 차를 출력한다