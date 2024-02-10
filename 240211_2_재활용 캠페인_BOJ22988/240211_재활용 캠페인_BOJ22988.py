# 재활용 캠페인_BOJ22988

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, X = map(int, input().split())            # N 용기의 수 / X 용기의 최대 용량을 input 받고
essence = list(map(int, input().split()))   # 용기에 남은 에센스의 양을 리스트로 input 받는다
essence.sort()                              # 에센스를 오름차순으로 정렬하고
ans = 0                                     # 정답을 저장할 변수를 생성하고
for i in range(N-1, -1, -1):                # 가장 많은 용량부터 반복하면서
    if essence[i] >= X:                     # 최대 용량 이상이라면
        ans += 1                            # 꽉찬 헤어에센스 용기를 1 추가하고
        essence.pop()                       # 리스트에서 빼준다
s = 0                                       # 가장 작은 용량을 가르키는 포인터를 생성하고
e = len(essence)-1                          # 가장 큰 용량을 가르키는 포인터를 생성한다
cnt = len(essence)                          # 남아있는 용기의 수를 저장한 변수를 생성하고
while s < e:                                # 두 포인터가 만날때까지 반복해서
    tmp = essence[e] + essence[s]           # e와 s가 가르키는 용량의 합을 구한 후
    if tmp >= X/2:                          # 두 용량의 합이 최대 용량의 절반 이상이라면
        ans += 1                            # 꽉찬 헤어에센스 용기를 1 추가하고
        cnt -= 2                            # 남은 용기의 수를 2개 빼준다
        e -= 1                              # 최소 용량을 가르키는 포인터를 한칸 이동하고
        s += 1                              # 최대 용량을 가르키는 포인터를 한칸 이동한다
    else:                                   # 두 용량의 합이 최대 용량의 절반보다 작다면
        s += 1                              # 최소 용량을 가르키는 포인터를 한칸 이동한다
print(ans + cnt // 3)                       # 꽉찬 용기의 수와 남은 용기 3개 당 하나씩 꽉찬 용기로 바꿀 수 있으므로 그 합을 출력한다