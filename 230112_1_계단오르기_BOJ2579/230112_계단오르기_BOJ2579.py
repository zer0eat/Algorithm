# 계단오르기_BOJ2579

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline().strip())           # 계단의 개수
step = []                                       # 계단 마다 점수를 저장할 리스트 생성
ans = [0]*T                                     # 각 계단마다 최고 점수를 저장할 리스트 생성
for t in range(T):                              # 계단의 수를 반복해서
    A = int(sys.stdin.readline().strip())       # A에 계단의 점수를 input 받고
    step.append(A)                              # step에 append

for t in range(T):                              # 계단의 수를 반복해서
    if t == 0:                                  # 첫번째 계단이면
        ans[t] = step[t]                        # ans에 첫번째 계단을 최고 점수로 저장
    elif t == 1:                                # 두번째 계단이면
        ans[t] = step[t] + ans[t-1]             # ans에 첫번째와 두번째 계단의 합을 최고 점수로 저장
    elif t == 2:                                # 세번째 계단이면
        if step[t-1] > step[t-2]:               # 첫번째와 두번째 계단을 비교하여 첫번째 계단의 점수가 더 크면
            ans[t] = step[t] + step[t-1]        # ans에 첫번째와 세번째 계단의 합을 저장하고
        else:                                   # 첫번째와 두번째 계단을 비교하여 두번째 계단의 점수가 같거나 더 크면
            ans[t] = step[t] + step[t-2]        # ans에 두번째와 세번째 계단의 합을 저장한다
    else:                                       # 4번째 이후 계단부터는
        A = ans[t-2] + step[t]                  # t번째 계단과 t-2까지의 최고점을 더한 값을 A
        B = ans[t-3] + step[t-1] + step[t]      # t번째 계단과 t-1계단의 점수를 더한 후 t-3까지의 최고점을 더한 값을 B라고 할 때
        if A > B:                               # A가 더크면
            ans[t] = A                          # ans에 A를 저장
        else:                                   # B가 같거나 더 크면
            ans[t] = B                          # ans에 B를 저장
print(ans[T-1])                                 # 마지막 계단의 최고점을 출력한다
