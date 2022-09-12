# 소수찾기_BOJ1978

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                        # 소수인지 검사할 숫자의 개수
arr = list(map(int, input().split()))   # 검사할 숫자열의 리스트

ans = 0                                 # 소수의 개수를 저장할 변수

for n in range(N):                      # 검사할 숫자만큼 반복할 때
    tmp = []                            # 임시 리스트를 생성하고
    t = 1                               # 검사할 숫자를 나눠줄 변수를 생성한 뒤
    while 1:                            # break가 나올때까지 반복해서
        if t > arr[n]:                  # 만약 나누어지는 수보다 t가 커지면 break
            break
        else:                           # t보다 나누어지는 수가 크다면
            if arr[n] % t == 0:         # t로 나누어 떨어지는 경우에
                tmp.append(t)           # tmp에 t를 append 하고
                t += 1                  # t를 하나 증가시킨다
            else:                       # 만약 나눠떨어지지 않는다면
                t += 1                  # t만 하나 증가시킨다
    if len(tmp) == 2:                   # 검사후 tmp에 2개만 담겨있다면 소수이므로
        ans += 1                        # 정답에 1을 추가한다

print(ans)