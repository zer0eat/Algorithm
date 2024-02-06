# 사냥꾼_BOJ8983

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M, N, L = map(int, input().split())                         # M 사로의 수 / N 동물의 수 / L 사거리를 input 받고
shoot = list(map(int, input().split()))                     # 사로의 x축을 리스트로 input 받는다
shoot.sort()                                                # 사로를 오름차순으로 정렬하고
ans = 0                                                     # 정답을 저장할 변수를 생성한다
for n in range(N):                                          # 동물의 수를 반복해서
    x, y = map(int, input().split())                        # 동물의 위치를 input 받는다
    if y <= L:                                              # y의 거리가 사거리 안에 있다면
        l = 0                                               # 사로의 왼쪽 인덱스를 저장한 변수를 생성하고
        r = M-1                                             # 사로의 오른쪽 인덱스를 저장한 변수를 생성한다
        start = x+y-L                                       # 동물을 잡을 수 있는 맨 왼쪽 사로를 저장하고
        end = x-y+L                                         # 동물을 잡을 수 있는 맨 오른쪽 사로를 저장한다
        while l <= r:                                       # 왼쪽 인덱스가 오른쪽 인덱스와 같거나 커질때까지 반복해서
            mid = (l+r)//2                                  # 인덱스의 중점을 저장하고
            if shoot[mid] >= start and shoot[mid] <= end:   # mid 인덱스의 사로가 start와 end 사이에 있다면
                ans += 1                                    # 잡을 수 있는 동물의 수를 추가하고
                break                                       # while문을 break한다
            elif shoot[mid] < start:                        # mid 인덱스의 사로가 start보다 작다면
                l = mid+1                                   # 왼쪽 인덱스를 증가시키고
            elif shoot[mid] > end:                          # mid 인덱스의 사로가 end보다 크면
                r = mid-1                                   # 오른쪽 인덱스를 감소시킨다
print(ans)                                                  # 잡을 수 있는 동물의 수를 출력한다