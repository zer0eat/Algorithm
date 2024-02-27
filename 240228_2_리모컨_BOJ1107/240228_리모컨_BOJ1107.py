# 리모컨_BOJ1107

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 이동하려는 채널을 input 받고
L = len(str(N))+1                               # 채널의 길이보다 1 큰수를 저장한 변수를 생성한다
M = int(input())                                # 고장난 버튼의 수를 input 받고
broken = list(map(int, input().split()))        # 고장난 버튼을 리스트로 input 받는다
ans = abs(N-100)                                # 이동버튼으로 이동할 수 있는 최솟값을 저장한 변수를 생성한다

def recur(dep, num):
    global ans                                  # ans를 global 변수로 선언하고
    if dep > 0:                                 # 숫자를 하나라도 눌렀다면
        ans = min(ans, abs(N-int(num))+dep)     # 해당 숫자에서 이동하는 횟수와 ans 중 더 작은 값을 저장한다
    if dep == L:                                # dep이 L과 같아졌다면
        return                                  # 이 이상은 최소가 나올 가능성이 없으므로 return한다
    for i in range(10):                         # 리모컨의 숫자를 반복해서
        if i in broken:                         # i가 고장난 숫자라면
            continue                            # continue하고
        recur(dep+1, num+str(i))                # 깊이 dep+1부터 최소 이동횟수를 탐색한다

recur(0, '')                                    # 깊이 0부터 최소 이동횟수를 탐색한다
print(ans)                                      # 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다