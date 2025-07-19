# 빅데이터 vs 정보보호 vs 인공지능_BOJ30957

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 학생의 수를 input받고
ans = [0]*3                 # 관심사를 저장할 리스트를 생성한다
L = list(input().strip())   # 관심사를 리스트로 input받고
for n in range(N):          # 학생의 수를 반복해서
    if L[n] == 'B':         # 빅데이터 관심사라면
        ans[0] += 1         # 첫번째에 추가하고
    elif L[n] == 'S':       # 정보보호 관심사라면
        ans[1] += 1         # 두번쨰에 추가하고
    elif L[n] == 'A':       # 인공지능 관심사라면
        ans[2] += 1         # 마지막에 추가한다
if ans[0] < ans[1]:         # 정보보호 관심사가 더 많다면
    if ans[1] < ans[2]:     # 인공지능 관심사가 더 많다면
        print('A')          # A를 출력한다
    elif ans[1] > ans[2]:   # 정보보호 관심사가 더 많다면
        print('S')          # S를 출력한다
    else:                   # 정보보호 인공지능 관심사가 같다면
        print('SA')         # SA를 출력한다
elif ans[0] > ans[1]:       # 빅데이터 관심시가 더 많다면
    if ans[0] < ans[2]:     # 인공지능 관심사가 더 많다면
        print('A')          # A를 출력한다
    elif ans[0] > ans[2]:   # 빅데이터 관심시가 더 많다면
        print('B')          # B를 출력한다
    else:                   # 빅데이터 인공지능 관심사가 같아면
        print('BA')         # BA를 출력한다
else:                       # 빅데이터 정보보호 관심사가 같다면
    if ans[0] < ans[2]:     # 인공지능 관심사가 더 많다면
        print('A')          # A를 출력한다
    elif ans[0] > ans[2]:   # 빅데이터 관심사가 더 많다면
        print('BS')         # BS를 출력한다
    else:                   # 빅데이터 정보보호 인공지능 관심사가 같다면
        print('SCU')        # SCU를 출력한다